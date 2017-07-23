import os, sys, argparse
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tensorflow as tf

from lib.config import params_setup
from lib.train import train
from lib.predict import predict
from lib.chat import chat
from lib.fight import fight
# from lib.mert import mert

def main(_):
        args = params_setup(model_num=0)
        args1 = params_setup(model_num=1)

        args = check_mion_ray(args)
        args1 = check_mion_ray(args1)

        print("[args]: ", args)
        if args.mode == 'train':
            train(args)
        elif args.mode == 'test':
            predict(args)
        elif args.mode == 'chat':
            chat(args)
        elif args.mode == 'fight':
            fight(args, args1)


def check_mion_ray(arg):
    try:
        mn = (args.model_name).split('_')[1]
    except:
        return arg
    return arg

if __name__ == "__main__":
        tf.app.run()