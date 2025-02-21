python train.py config/train_book.py --device=mps --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=64 --n_layer=4 --n_head=4 --n_embd=32 --max_iters=7500 --lr_decay_iters=7500 --dropout=0.0 
#python train.py config/train_book.py --device=mps --compile=False --eval_iters=20 --log_interval=1 --block_size=128 --batch_size=64 --n_layer=4 --n_head=4 --n_embd=32 --max_iters=7500 --lr_decay_iters=7500 --dropout=0.0 --init_from='reset'

#python train.py config/train_book.py --device=mps --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=64 --n_layer=5 --n_head=5 --n_embd=160 --max_iters=5000 --lr_decay_iters=5000 --dropout=0.0 --wandb_run_name=minigpt5 

# 5M
#python train.py config/train_book.py --device=mps --compile=False --eval_iters=20 --log_interval=1 --block_size=128 --batch_size=32 --n_layer=5 --n_head=5 --n_embd=160 --max_iters=7500 --lr_decay_iters=7500 --dropout=0.2 --wandb_run_name=minigpt5-longer2 

#python train.py config/train_book.py --device=mps --compile=False --eval_iters=20 --log_interval=1 --wandb_run_name=minigpt5-big2 
