from sklearn.datasets import fetch_olivetti_faces
from sklearn.ensemble import RandomForestClassifier
import time
import matplotlib.pyplot as plt

n_jobs = -1

data = fetch_olivetti_faces()
X,y = data.data, data.target

mask = y<5
X = X[mask]
y = y[mask]

forest = RandomForestClassifier(n_estimators=750, n_jobs=n_jobs, random_state=42)

forest.fit(X,y)
start_time = time.time()
img_shape = data.images[16].shape
importances = forest.feature_importances_
elapsed_time = time.time() - start_time

print(f"czas obliczenia istotnych pikseli: {elapsed_time:.3f} sekund")
imp_reshaped = importances.reshape(img_shape)

plt.matshow(imp_reshaped, cmap = plt.cm.hot)
plt.title("istotne piksele obliczone przy użyciu wartości zanieczyszczeń")
plt.colorbar()
plt.show()
