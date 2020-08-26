import igraph as ig

# Gera o Grafo
g = ig.Graph.Read('0.edges')

# Pega a distribuições dos graus
degree_distributions = ig.Graph.degree_distribution(g)

# Pega os caminhos mínimos
minimum_paths = g.path_length_hist(directed=False)

# Plot das distribuições dos graus
ig.plot(degree_distributions)
# Salva a imagem 
ig.plot(degree_distributions, 'degree_distributions.png')

# Plot dos caminhos mínimos
ig.plot(minimum_paths)
# Salva a imagem 
ig.plot(minimum_paths, 'minimum_paths.png')

# Pega a distribuições a média dos graus
average_path_length = ig.Graph.average_path_length(g)
print('Média dos graus:', average_path_length)
print('\n\n')

# Pega a quantidade de componentes conectados
connected_components = ig.Graph.components(g)
print('Quantidade de componentes conectados:', connected_components[0])
print('\n\n')

# Pega o tamanho do maior componente conectado
largest_connected_components = ig.Graph.omega(g)
print('Tamanho do maior componente conectado:', largest_connected_components)
print('\n\n')