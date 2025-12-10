---
title: "A Study on the Relevance of Generic Word Embeddings for Sentence Classification in Hepatic Surgery"
authors:
  - Achir Oukelmoun
  - Nasredine Semmar
  - Gaël De Chalendar
  - Enguerrand Habran
  - Eric Vibert
  - Emma Goblet
  - Mariame Oukelmoun
  - Marc-Antoine Allard
date: 2023-01-01
venue: "2023 20th {ACS}/{IEEE} International Conference on Computer Systems and Applications ({AICCSA})"
venue_short: "ICCSA"
type: conference
selected: false
links:
  paper: https://ieeexplore.ieee.org/abstract/document/10479342
---

While the fine-tuning process of extensive contextual language models often demands substantial computational capacity, utilizing generic pre-trained models in highly specialized domains can yield suboptimal results. This paper aims to explore an innovative approach to derive pertinent word embeddings tailored to a specific domain with limited computational resources (The introduced methodologies are tested within the domain of hepatic surgery, utilizing the French language.). This exploration takes place within a context where computational limitations prohibit the fine-tuning of large language models. A new embedding (referred to as {FTW}2V) that combines Word2Vec and {FastText} is introduced. This approach addresses the challenge of incorporating terms absent from Word2Vec’s vocabulary. Furthermore, a novel method is used to evaluate the significance of word embeddings within a specialized corpus. This evaluation involves comparing classification scores distributions of classifiers (Gradient Boosting) trained on word embeddings derived from benchmarked Natural Language Processing ({NLP}) models. As per this assessment technique, the {FTW}2V model, trained from scratch with limited computational resources, outperforms generic contextual models in terms of word embeddings quality. Additionally, a computationally efficient contextual model rooted in {FTW}2V is introduced. This modified model substitutes Gradient Boosting with a transformer and integrates Part Of Speech labels.
