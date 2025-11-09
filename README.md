
# Shopper Spectrum:
## Customer Segmentation & Product Recommendations 🛒

## Project Overview  

In this project, we apply customer segmentation and recommendation-system techniques to e-commerce data to drive actionable insights and help improve product targeting.  
We perform RFM (Recency-Frequency-Monetary) analysis to segment customers, followed by an item-based recommendation system using cosine similarity for generating product suggestions.

## Key Techniques Used  
- **Customer Segmentation via RFM**:We calculate recency, frequency and monetary values for each customer and assign them to different segments (e.g, High-Value/Champions,Loyal / Regular, Occasional, At-Risk).

  
- **Item-based Recommendation System**:We build a product-to-product similarity model using cosine similarity on item feature vectors, enabling us to recommend items similar to those a customer has already interacted with.

###  Customer Segmentation (RFM)  
 1. Cleaned transactional data: handled outliers & anomalies, scaled features.  
 2. Calculated Recency, Frequency & Monetary (R / F / M) scores for each customer.  
 3. Assigned customers into segments based on RFM (e.g.,  High-Value/Champions, Loyal/Regular, Occasional, At-Risk).
 4. Analysed segment profiles to identify high-value and growth-opportunity groups.  
 5. Visualised segment distributions and spending behaviour for business insight.  

###  Recommendation System (Item-based using Cosine Similarity)  
  1. Built an item-interaction matrix capturing user-item purchase behaviour.  
  2. Computed item-to-item similarity using cosine similarity metric.  
  3. Generated product recommendations: for a given item, retrieved 5 top similar items.  
  4. Deployed as interactive dashboard using Streamlit for real-time product suggestions.  


## Result Snapshot  
![Project Output](assets/images/output_screenshot.png)  

