class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

Pg = City('Praia Grande', 'Brasil', 365.577, ['Beach', 'Litoral Plaza Shopping'])
Detroit = City('Detroit', 'United State', 645.705, ['Comerica Park', 'Motown Museum'])
Amityville = City('Amityville', 'United States of America', 9.718, ['Bragino Creations', 'The Spa Haus'])

print(vars(Pg))
print(vars(Detroit))
print(vars(Amityville))