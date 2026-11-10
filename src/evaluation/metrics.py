from sklearn.metrics import roc_auc_score, f1_score, confusion_matrix

def binary_metrics(y_true, y_pred, y_score=None):
    output = {
        "f1": f1_score(y_true, y_pred, zero_division=0),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
    }
    if y_score is not None and len(set(y_true)) == 2:
        output["image_auroc"] = roc_auc_score(y_true, y_score)
    return output
