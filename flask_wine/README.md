## Wine Predictor

This project is a wine predictor based on the dataset "winemag-data-130k-v2.csv" (50.46 MB)
The dataset is available on Kaggle : https://www.kaggle.com/zynicide/wine-reviews
Our model as been trained only on French Wines (data set with 22093 entries, training set (80%) = 15173 entries)


To run the programm please go on the right folder and enter :
python main.py

The app should be available on :
http://0.0.0.0:5000/


On the main page, you should enter the following informations :

* Wine Price (must be a float)

* Wine Province
EX : Rhône Valley, Burgundy, Alsace

* Wine Variety (french "cépage")
EX : Rhône-style Red Blend, Pinot Noir, Chardonnay

* Winery
EX : Famille Perrin

* Wine Region_1 (french "AOC")
EX : Vacqueyras, Alsace, Sancerre


Launch the prediction...
You will get a score. The closer 100, the better !!


You can test with the following entries :

[nan, 'Burgundy', 'Pinot Noir', 'Henri de Villamont', 'Grands-Echezeaux', 94]
[35.0, 'Bordeaux', 'Bordeaux-style Red Blend', 'Château de Côme', 'Saint-Estèphe', 90]
[18.0, 'Provence', 'Rosé', 'Château Thuerry', 'Côtes de Provence', 87]
[13.0, 'Beaujolais', 'Gamay', 'Georges Duboeuf', 'Beaujolais-Villages', 86]
[51.0, 'Rhône Valley', 'Rhône-style Red Blend', 'Tardieu-Laurent', 'Gigondas', 89]
[150.0, 'Champagne', 'Champagne Blend', 'Perrier Jouët', 'Champagne', 95]
[20.0, 'Bordeaux', 'Bordeaux-style Red Blend', 'Château Tour Saint-Germain', 'Blaye Côtes de Bordeaux', 83]
[nan, 'Loire Valley', 'Sauvignon Blanc', 'De Ladoucette', 'Pouilly-Fumé', 89]
[65.0, 'Burgundy', 'Chardonnay', 'Louis Max', 'Mercurey', 90]
[450.0, 'Burgundy', 'Pinot Noir', 'Philippe Pacalet', 'Echézeaux', 94]
[15.0, 'Rhône Valley', 'Rhône-style Red Blend', 'Château de Nages', 'Costières de Nîmes', 91]
[nan, 'Burgundy', 'Chardonnay', 'Patrick Javillier', 'Puligny-Montrachet', 94]
[13.0, 'Provence', 'Rosé', 'Domaines Pierre Chavin', 'Côtes de Provence', 86]
[25.0, 'Bordeaux', 'Bordeaux-style Red Blend', 'Château des Annereaux', 'Lalande de Pomerol', 88]
[71.0, 'Burgundy', 'Chardonnay', 'Xavier Monnot', 'Meursault', 91]
[23.0, 'Burgundy', 'Chardonnay', 'Verget', 'Mâcon-Charnay', 88]
[100.0, 'Champagne', 'Chardonnay', 'Château de Bligny', 'Champagne', 91]
[nan, 'Burgundy', 'Chardonnay', 'Jean-Claude Debeaune', 'Saint-Véran', 86]
[7.0, 'Bordeaux', 'Bordeaux-style White Blend', 'Calvet', 'Bordeaux Blanc', 85]
[100.0, 'Bordeaux', 'Bordeaux-style Red Blend', 'Château Giscours', 'Margaux', 94]
[111.0, 'Rhône Valley', 'Rhône-style Red Blend', 'Domaine du Pegau', 'Châteauneuf-du-Pape', 94]
[20.0, 'Loire Valley', 'Sauvignon Blanc', 'Florian Roblin', 'Coteaux du Giennois', 87]
[nan, 'Languedoc-Roussillon', 'Rhône-style Red Blend', 'Château Maylandie', 'Corbières-Boutenac', 91]
[60.0, 'Languedoc-Roussillon', 'Rhône-style Red Blend', 'Domaine Thunevin-Calvet', 'Côtes du Roussillon Villages', 93]
[79.0, 'Champagne', 'Chardonnay', 'Delamotte', 'Champagne', 93]
[22.0, 'Loire Valley', 'Sauvignon Blanc', 'Dominique Pabiot', 'Pouilly-Fumé', 88]
[25.0, 'Loire Valley', 'Rosé', 'Domaine des Grandes Perrières', 'Sancerre', 88]
[nan, 'Burgundy', 'Chardonnay', 'Albert Bichot', 'Savigny-lès-Beaune', 88]
[11.0, 'Bordeaux', 'Rosé', 'Quai de la Lune', 'Bordeaux Rosé', 88]
[35.0, 'Alsace', 'Riesling', 'Maurice Schoech & Fils', 'Alsace', 93]
[27.0, 'Loire Valley', 'Pinot Noir', 'Henri Bourgeois', 'Sancerre', 88]
[95.0, 'Champagne', 'Champagne Blend', 'Taittinger', 'Champagne', 94]
[14.0, 'Alsace', 'White Blend', 'Pierre Sparr', 'Alsace', 85]
[60.0, 'Burgundy', 'Chardonnay', 'Chanson Père et Fils', 'Savigny-lès-Beaune', 87]
[nan, 'Bordeaux', 'Bordeaux-style Red Blend', 'Le Petit Cheval', 'Saint-Émilion', 92]
[nan, 'Burgundy', 'Chardonnay', 'Georges Duboeuf', 'Pouilly-Fuissé', 88]
[14.0, 'Loire Valley', 'Melon', 'Château de la Ragotiere', 'Muscadet Sèvre et Maine', 88]
[40.0, 'Burgundy', 'Chardonnay', 'Louis Latour', 'Montagny', 88]
[22.0, 'Bordeaux', 'Bordeaux-style Red Blend', 'Château Gressier Grand Poujeaux', 'Moulis-en-Médoc', 89]
[163.0, 'Bordeaux', 'Bordeaux-style Red Blend', 'Château Canon', 'Saint-Émilion', 95]
[55.0, 'Burgundy', 'Pinot Noir', 'Pierre André', 'Volnay', 91]
[35.0, 'Bordeaux', 'Bordeaux-style Red Blend', 'Château Lilian Ladouys', 'Saint-Estèphe', 94]
[21.0, 'Alsace', 'Pinot Gris', 'Dopff & Irion', 'Alsace', 89]
[15.0, 'Beaujolais', 'Gamay', 'Domaine Pral', 'Beaujolais', 85]
[55.0, 'Champagne', 'Champagne Blend', 'Jean Milan', 'Champagne', 88]
[19.0, 'Beaujolais', 'Gamay', 'Domaine Dumas', 'Brouilly', 89]
[46.0, 'Rhône Valley', 'Syrah', 'Tardieu-Laurent', 'Saint-Joseph', 91]
[nan, 'Bordeaux', 'Bordeaux-style Red Blend', 'Château de Malleret', 'Haut-Médoc', 91]
[120.0, 'Burgundy', 'Pinot Noir', 'Domaine des Perdrix', 'Nuits-St.-Georges', 91]
[14.0, 'Alsace', 'White Blend', 'Domaine Bott-Geyl', 'Alsace', 91]
[28.0, 'Provence', 'Provence red blend', 'Commanderie de la Bargemone', "Coteaux d'Aix-en-Provence", 92]
[13.0, 'Bordeaux', 'Bordeaux-style Red Blend', 'Etablissements Thunevin', 'Bordeaux', 87]
[40.0, 'Burgundy', 'Chardonnay', 'Joseph Drouhin', 'Chablis', 92]
[nan, 'Alsace', 'Riesling', 'André Blanck et ses Fils', 'Alsace', 86]
[27.0, 'Loire Valley', 'Sauvignon Blanc', 'François Millet', 'Sancerre', 88]
[15.0, 'Burgundy', 'Chardonnay', 'Vignerons de Bel Air', 'Coteaux Bourguignons', 85]
[50.0, 'Burgundy', 'Chardonnay', 'Domaine Vrignaud', 'Chablis', 85]
[13.0, 'Loire Valley', 'Melon', 'Domaine du Colombier', 'Muscadet Sèvre et Maine', 86]
[nan, 'France Other', 'Savagnin', 'Domaine Buronfosse', 'Côtes du Jura', 90]
[62.0, 'Champagne', 'Chardonnay', 'G. H. Mumm', 'Champagne', 92]
[69.0, 'Burgundy', 'Chardonnay', 'La Chablisienne', 'Chablis', 94]
[70.0, 'Champagne', 'Champagne Blend', 'Castelnau', 'Champagne', 90]
[12.0, 'Rhône Valley', 'Grenache-Syrah', 'Château Grande Cassagne', 'Costières de Nîmes', 87]
[25.0, 'Bordeaux', 'Bordeaux-style Red Blend', 'Château Frédignac', 'Blaye Côtes de Bordeaux', 88]
[55.0, 'Alsace', 'Pinot Noir', 'Hugel', 'Alsace', 94]
