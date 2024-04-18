import time
log_interval = 10 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = True # override via command line if you like
out_dir = 'out_book_gpt2'
eval_interval = 100
eval_iters = 10

wandb_project = 'shakespeare'
wandb_run_name = 'ft1-' + str(time.time())

dataset = 'bookgpt'
init_from = 'gpt2' # this is the largest GPT-2 model
reset_vocab=True
# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 32
block_size= 128
gradient_accumulation_steps = 2
max_iters = 300

# finetune at constant LR
learning_rate = 3e-5
decay_lr = False
