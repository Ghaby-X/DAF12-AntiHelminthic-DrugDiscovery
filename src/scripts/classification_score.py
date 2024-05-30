from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_auc_score
def classification_score(y_test, y_pred):
    return {
        'accuracy': accuracy_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'f1_score': f1_score(y_test, y_pred),
        'roc_auc_score': roc_auc_score(y_test, y_pred),
    }