import config
import pickle

class SVD_Model:
    def load_model(self):
        with open(config.MODEL_PATH, 'rb') as f:
            self.model = pickle.load(f)['svd_model']

            
    def predict(self, user_id: int, item_id: int) -> float:
        """
        Predicts the rating of an item for a given user id.

        Args:
            model: A trained model that can make predictions.
            uid (int): The ID of the user for whom to predict the rating.
            iid (int): The ID of the item for which to predict the rating.

        Returns:
            float: The predicted rating of the item for the given user.
        """

        pred = self.model.predict(user_id, item_id)
        return pred.est
    
