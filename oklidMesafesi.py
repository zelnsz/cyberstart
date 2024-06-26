import math

# Noktalar listesi tanımlanır
points = [(0, 0), (3, 4)]

# İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon yazılır : euclideanDistance
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2) #ölkid bulmak için gereken formül

# tüm nokta çiftleri arasındaki mesafeleri hesaplayıp saklamak için:
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulup yazdırma
min_distance = min(distances)
print(f'En kısa mesafe: {min_distance}')
