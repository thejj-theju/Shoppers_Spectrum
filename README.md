
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

1. Customer segmentation Tab:


<img width="1917" height="782" alt="Screenshot 2025-11-10 192233" src="https://github.com/user-attachments/assets/8d6a39c5-d50a-4d64-88c1-0790c293247e" />


2. Product Recommendation Tab:
   

<img width="1908" height="791" alt="Screenshot 2025-11-10 192254" src="https://github.com/user-attachments/assets/8cf1508f-29ab-411f-abbd-5d3535269374" />

3. Summary of the Datasets and Visualization Part:

   
<img width="1919" height="786" alt="Screenshot 2025-11-10 192328" src="https://github.com/user-attachments/assets/1ad14292-b33b-48de-b450-9170b4c7874c" />

<img width="1366" height="737" alt="Screenshot 2025-11-10 192601" src="https://github.com/user-attachments/assets/dc8ccc87-966a-455c-92a3-17f9b175b0a0" />

<img width="1411" height="734" alt="Screenshot 2025-11-10 192420" src="https://github.com/user-attachments/assets/8088a59d-d72e-4c08-a0ba-984887cf93a6" />


<img width="1449" height="729" alt="Screenshot 2025-11-10 192534" src="https://github.com/user-attachments/assets/5079ece6-f64e-4580-808e-a5ed77f0fb4e" />


<img width="1431" height="732" alt="Screenshot 2025-11-10 192353" src="https://github.com/user-attachments/assets/a41bfedd-538e-4621-b143-24e0b4482687" />



