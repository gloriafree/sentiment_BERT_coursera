# Hugging face
it provides a bunch of libraries for SOTA transformer (TF 2.0) models (like BERT, GPT2, RoBERTa, etc) and pre-trained model weights


# consistently seed the process
*good practice is to always seed the process consistently*
torch.cuda.manual_seed_all is to configure seed when you use GPU

# train models

# define train loss function
initialize training loss to be 0

# create a progress bar using tqdm
it provides a simple progress bar with estimation time to finish


# in order to fine-tune model, we configure an optimizer and scheduler
Within each epoch, for every batch, we set up loss function to aggregate loss.
