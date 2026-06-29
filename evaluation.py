# services/evaluation.py

def evaluate_count(
    true_positive,
    false_positive,
    false_negative
):

    precision = (
        true_positive /
        (true_positive +
         false_positive)
    )

    recall = (
        true_positive /
        (true_positive +
         false_negative)
    )

    f1 = (
        2 *
        precision *
        recall
    ) / (
        precision +
        recall
    )

    return {
        "precision":
            round(
                precision * 100,
                2
            ),

        "recall":
            round(
                recall * 100,
                2
            ),

        "f1_score":
            round(
                f1 * 100,
                2
            )
    }

metrics = evaluate_count(
    true_positive=90,
    false_positive=10,
    false_negative=15
)

print(metrics)