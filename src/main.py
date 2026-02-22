from src.data_loader import get_dataloaders
from src.train import train
from src.inference import classify_image
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["train", "infer"], required=True)
    parser.add_argument("--image", type=str, help="for infer")
    args = parser.parse_args()
    
    if args.mode == "train":
        train()
    else:
        result = classify_image(args.image)
        print(f"Class: {result}")