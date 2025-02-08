# Page View Time Series Visualizer

This is the boilerplate for the Page View Time Series Visualizer project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/page-view-time-series-visualizer


# **📊 Visualisation des séries temporelles des vues de page**

Dans ce projet, vous allez travailler avec notre code de démarrage **Gitpod**.

Nous sommes encore en train de développer la partie interactive du programme Python. En attendant, voici quelques vidéos sur la chaîne YouTube de **freeCodeCamp.org** qui vous apprendront tout ce dont vous avez besoin pour compléter ce projet :

- **Python for Everybody** (Cours vidéo - 14 heures)  
- **How to Analyze Data with Python Pandas** (10 heures)

---

## **📌 Objectif du projet**  
Vous allez **visualiser des données temporelles** en utilisant :  
- un **line chart** (*graphique en ligne*),  
- un **bar chart** (*diagramme en barres*),  
- des **box plots** (*boîtes à moustaches*).  

Vous utiliserez **Pandas, Matplotlib et Seaborn** pour visualiser un dataset contenant le **nombre de vues de page** sur le forum **freeCodeCamp.org** chaque jour entre **le 9 mai 2016 et le 3 décembre 2019**.  

Les visualisations de données vous aideront à **analyser les tendances des visites** et à identifier la **croissance annuelle et mensuelle**.

---

## **📌 Tâches à accomplir**  

### **1️⃣ Importer et nettoyer les données**  
✅ Utiliser **Pandas** pour **importer** les données depuis le fichier **"fcc-forum-pageviews.csv"** et **définir l’index** sur la colonne des **dates**.  

✅ Nettoyer les données en supprimant les jours où les vues de pages sont dans les **2,5 % supérieurs** et **2,5 % inférieurs** du dataset.

---

### **2️⃣ Créer un graphique en ligne (line chart)**
✅ Implémenter une fonction **`draw_line_plot()`** qui utilise **Matplotlib** pour dessiner un **line chart** (*graphique en ligne*) similaire à `"examples/Figure_1.png"`.  

✅ Le graphique doit avoir :  
- **Titre** : *Daily freeCodeCamp Forum Page Views 5/2016-12/2019*  
- **Axe X (horizontal)** : *Date*  
- **Axe Y (vertical)** : *Page Views*  

---

### **3️⃣ Créer un diagramme en barres (bar chart)**  
✅ Implémenter une fonction **`draw_bar_plot()`** qui génère un **bar chart** (*diagramme en barres*) similaire à `"examples/Figure_2.png"`.  

✅ Ce diagramme doit montrer la **moyenne des vues de page par mois**, regroupée par **année**.  

✅ Le graphique doit inclure :  
- **Légende** : doit afficher les noms des **mois**, avec le titre **"Months"** (*Mois*).  
- **Axe X (horizontal)** : *Years* (*Années*).  
- **Axe Y (vertical)** : *Average Page Views* (*Moyenne des vues de page*).  

---

### **4️⃣ Créer des box plots pour analyser les tendances**
✅ Implémenter une fonction **`draw_box_plot()`** qui utilise **Seaborn** pour dessiner **deux box plots adjacents** (*boîtes à moustaches*), similaires à `"examples/Figure_3.png"`.  

✅ Ces **box plots** doivent montrer :  
1. **Comment les valeurs sont distribuées chaque année** 📊  
   - **Titre du graphique** : *Year-wise Box Plot (Trend)* (*Box Plot annuel - Tendance*)  
2. **Comment les valeurs varient selon le mois** 📉  
   - **Titre du graphique** : *Month-wise Box Plot (Seasonality)* (*Box Plot mensuel - Saisonnalité*)  

✅ Assurez-vous que :  
- Les **mois** sur l’axe X commencent par **Janvier (Jan)**.  
- Les **axes X et Y** sont correctement **nommés**.  
- Utilisez une **copie du DataFrame** pour éviter de modifier les données originales.  

---

## **📌 Finalisation et sauvegarde des graphiques**
Le **code de base (boilerplate)** inclut également des commandes pour :  
✅ **Préparer les données** pour les visualisations.  
✅ **Sauvegarder et retourner** chaque **graphique sous forme d’image**.

---

🚀 **Avec ce projet, vous allez apprendre à :**  
✅ Manipuler et nettoyer des données temporelles avec **Pandas**.  
✅ Visualiser des tendances avec **Matplotlib** et **Seaborn**.  
✅ Comprendre la saisonnalité et l’évolution des données avec des **box plots**.  

Bonne analyse et bon code ! 💡📊