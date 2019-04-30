"""Evaluate and test the model with the dataset parameter name"""

import sys
import os
import argparse

try:
    sys.path[0] = os.path.join(sys.path[0], "..")
    from environment import setup_path
    from data.generator import DataGenerator
    from network.network import HTRNetwork
except ImportError as exc:
    sys.exit(f"Import error in '{__file__}': {exc}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--batch", type=int, required=True)
    args = parser.parse_args()
    args = setup_path(args)

    dtgen = DataGenerator(args, test=True)
    htr = HTRNetwork(dtgen)
    htr.model.summary()

    # eval = htr.model.evaluate(
    #     x=dtgen.next_eval(),
    #     batch_size=dtgen.batch_size,
    #     metrics=["loss", "ler", "ser"],
    #     verbose=1
    # )

    # # Outputs: a list containing:
    # #   loss (number)
    # #   label error rate for esach data (list)
    # #   sequence error rate on the dataset
    # print("\n", eval, "\n")

    # pred = htr.model.predict(
    #     x=dtgen.next_pred(),
    #     batch_size=dtgen.batch_size,
    #     max_value=dtgen.padding_value,
    #     verbose=1
    # )

    # for i in range(len(pred)):
    #     print("Prediction :", [j for j in pred[i] if j != -1], "-- Label :", dtgen.y_test[i])

    # # # create call back to save model, evaluation and predicts ###
    # # htr.model.save_model(path_dir=output + "models", charset=dtgen.dictionary)