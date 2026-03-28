"""
Scaffolding for TE_CORE Ordinative AI Fine-Tuning using Unsloth.
Model: Llama-3-8B-Instruct
Format: ChatML
"""
import torch
from unsloth import FastLanguageModel
from datasets import load_dataset
from trl import SFTTrainer
from transformers import TrainingArguments

max_seq_length = 4096 
dtype = None # Auto detection
load_in_4bit = True # Use 4bit quantization to reduce memory usage

# 1. Load the Base Model and Tokenizer
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/llama-3-8b-Instruct-bnb-4bit",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)

# 2. Add LoRA Adapters
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, 
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, 
    bias = "none",  
    use_gradient_checkpointing = "unsloth",
    random_state = 3407,
)

# 3. Format the Dataset (ChatML parsing)
from unsloth.chat_templates import get_chat_template

tokenizer = get_chat_template(
    tokenizer,
    chat_template = "chatml", 
    mapping = {"role" : "role", "content" : "content", "user" : "user", "assistant" : "assistant"}, 
)

def formatting_func(examples):
    texts = [tokenizer.apply_chat_template(convo, tokenize=False, add_generation_prompt=False) for convo in examples["messages"]]
    return {"text": texts}

# Load from the TE dataset generated
dataset = load_dataset("json", data_files={"train": "dataset/sample_TE_instruct.jsonl"})["train"]
dataset = dataset.map(formatting_func, batched = True)

# 4. Initialize SFTTrainer
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    dataset_num_proc = 2,
    packing = False, 
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        max_steps = 60,
        learning_rate = 2e-4,
        fp16 = not torch.cuda.is_bf16_supported(),
        bf16 = torch.cuda.is_bf16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
    ),
)

# 5. Start Training
trainer_stats = trainer.train()

# 6. Save Model
model.save_pretrained("lora_model_te_ordinative")
tokenizer.save_pretrained("lora_model_te_ordinative")
print("LoRA Adapter saved to /lora_model_te_ordinative")
