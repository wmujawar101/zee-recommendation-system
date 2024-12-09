import config
import pickle

class Similarity_Model:
        
    def load_model(self, model_type, similarity_matrix):
        """
        Load a pre-trained model based on the specified similarity matrix and model type.

        Args:
            model_type (str): The type of model to load (expected values are 'cosine' or 'pearson').
            similarity_matrix (str): The name of the similarity matrix to use (Expected values are 'user'or 'item').
            
        Returns:
            None
        """
        
        self.similarity_matrix = similarity_matrix.lower()
        self.model_type = model_type.lower()
        
        # Define model name
        model_name = f'{self.model_type}_similarity_{self.similarity_matrix}'
        
        # Read Model
        with open(config.MODEL_PATH, 'rb') as f:
            self.model = pickle.load(f)[model_name]
        
        
    
    def get_top_n_recommendations(self, idx, n=5):
        """
        Retrieve the top N most similar indices for a given index.
        
        Args:
            idx (int): The index to retrieve recommendations for.
            n (int, optional): The number of top recommendations to return. Defaults to 5.

        Returns:
            pd.Series: A Series containing the top N similar indices and their similarity scores, sorted in descending order.
        
        Raises:
            KeyError: If the specified index is not found in the model's columns.
        """
        
        if idx not in self.model.columns:
            return f"{self.model_type} '{idx}' not found in the dataset."

        similar_idx = self.model[idx]

        sorted_similar_idx = similar_idx.drop(idx).sort_values(ascending=False)

        top_similar_idx = sorted_similar_idx.head(n)

        return top_similar_idx.index.tolist()
