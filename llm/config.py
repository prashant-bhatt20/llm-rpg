import os
from pathlib import Path

REPO_DIR = Path(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

# Text extraction
#url = 'https://gosafir.com/mag/wp-content/uploads/2019/12/Tolkien-J.-The-lord-of-the-rings-HarperCollins-ebooks-2010.pdf'
url = 'https://ml-sampledataset.s3.us-west-2.amazonaws.com/LTIMindtree-Reports-Strong-Performance-in-Q3-FY23.pdf'
header_height = 20 # Main text distance from the top of the page: to remove header
footer_height = 594 # Remove footer
start_page = 2
end_page = 16
extraction_path = REPO_DIR / "llm/data/extracted_text.jsonl"

# Text processing
min_length = 10

# HF repo
#hf_repo = "JeremyArancio/llm-tolkien"
hf_repo = "Prashantbhatt20/llm-tolkien"

# Dataset
context_length = 2048
batch_size = 5
test_size = 0.2
shuffle = True

# Training
model_name = 'bigscience/bloom-3b'
lora_r = 16 # attention heads
lora_alpha = 32 # alpha scaling
lora_dropout = 0.05
lora_bias = "none"
lora_task_type = "CAUSAL_LM" # set this for CLM or Seq2Seq

## Trainer config
per_device_train_batch_size = 1 
gradient_accumulation_steps = 1
warmup_steps = 100 
num_train_epochs=3
weight_decay=0.1
learning_rate = 2e-4 
fp16 = True
logging_steps = 1
overwrite_output_dir = True
evaluation_strategy = "no"
save_strategy = "no"
push_to_hub = False

## Data collator
mlm =False

## Generate
max_new_tokens = 50
temperature = 0.5
do_sample = False

