import torch

# Check if GPU is available
if torch.cuda.is_available():
  print("GPU is available!")
  device = torch.device("cuda")  # Use GPU for computations
else:
  print("GPU is not available. Using CPU instead.")
  device = torch.device("cpu")  # Use CPU for computations