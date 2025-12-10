---
selected: true
title: "X-RiSAWOZ: High-Quality End-to-End Multilingual Dialogue Datasets and Few-shot Agents"
authors:
  - Mehrad Moradshahi
  - Tianhao Shen
  - Kalika Bali
  - Monojit Choudhury
  - Gael Chalendar
  - Anmol Goel
  - Sungkyun Kim
  - Prashant Kodali
  - Ponnurangam Kumaraguru
  - Nasredine Semmar
  - Sina Semnani
  - Jiwon Seo
  - Vivek Seshadri
  - Manish Shrivastava
  - Michael Sun
  - Aditya Yadavalli
  - Chaobin You
  - Deyi Xiong
  - Monica Lam
date: 2023-01-01
venue: "Findings of the {Association} for {Computational} {Linguistics}: {ACL} 2023"
venue_short: "Findings {Association}"
type: conference
links:
  paper: https://aclanthology.org/2023.findings-acl.174
---

Task-oriented dialogue research has mainly focused on a few popular languages like English and Chinese, due to the high dataset creation cost for a new language. To reduce the cost, we apply manual editing to automatically translated data. We create a new multilingual benchmark, X-RiSAWOZ, by translating the Chinese RiSAWOZ to 4 languages: English, French, Hindi, Korean; and a code-mixed English-Hindi language.X-RiSAWOZ has more than 18,000 human-verified dialogue utterances for each language, and unlike most multilingual prior work, is an end-to-end dataset for building fully-functioning agents. The many difficulties we encountered in creating X-RiSAWOZ led us to develop a toolset to accelerate the post-editing of a new language dataset after translation. This toolset improves machine translation with a hybrid entity alignment technique that combines neural with dictionary-based methods, along with many automated and semi-automated validation checks. We establish strong baselines for X-RiSAWOZ by training dialogue agents in the zero- and few-shot settings where limited gold data is available in the target language. Our results suggest that our translation and post-editing methodology and toolset can be used to create new high-quality multilingual dialogue agents cost-effectively. Our dataset, code, and toolkit are released open-source.
