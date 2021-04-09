---
title: ¿Cómo ganar en Overcooked con computación cuántica?
date: 2021-03-20 20:00:00 +/-0600
categories: [Computación Cuántica]
tags: [quantum-computing, quantum-mechanics, optimization, minimum-energy]
thumbnail: /assets/img/chefs/cover.jpg
math: true
---

Si reconocen la imagen principal de este post, es porque ya se han enfrentado a situaciones con un alto nivel de estrés en donde las cosas pueden seguir una vertiente caótica en cuestión de un parpadeo o un pequeño descuido. Pero, hey, "las risas no faltaron", ¿cierto?

Me refiero al caótico juego de cocina cooperativa "Overcooked" en donde tienes que hacer equipo con el resto de tus compañeros chefs para despachar las órdenes que te van pidiendo en una carrera contra el tiempo donde cada platillo requiere seguir una serie de pasos para su preparación. Este juego representa ni más ni menos que un problema de optimización justo como los que se pueden resolver con [Quantum Annealing](/posts/quantum_annealing/), así que ahora abordaremos el cómo plantear este problema para que la siguiente vez que vayamos a jugar con nuestros amigos, podamos sacar nuestra computadora cuántica y utilizarla para ganar.

Esta vez habrá un poco de todo: math por aquí, física por allá y algunas líneas de código por acá (sí, vamos a ver cómo simular el problema y cómo ejecutarlo en una computadora cuántica), pero el puro planteamiento ya es muy interesante de por sí y será el tema central del tema. Pueden saltarse lo demás si gustan.

![Overcooked](/assets/img/chefs/cover.jpg)
_Overcooked de Ghost Town Games Ltd._

## ¿Qué es Overcooked?

El primer paso para plantear el problema es entenderlo, así que vamos a empezar explicando (con algunas simplificaciones) la esencia de Overcooked:

En la parte superior de la pantalla, nos van apareciendo una lista de $$N$$ platillos que debemos preparar y despachar. Cada platillo requiere ejectuar un mini-algoritmo diferente para poder prepararlo que va desde recolectar los ingredientes, picarlos, cocinarlos y ponerlos en un platito que hay que depositar en una banda transportadora.

La situación se complica cuando tenemos un equipo de $$m$$ chefs (algunos no humanos) que tienen que repartirse las partes de cada algoritmo para poder despachar un platillo en el menor tiempo posible. Además, podemos suponer que todos los chefs van a poder estar trabajando en algo de manera simultanea (es decir, siempre van a estar ocupados).

Para los propósitos de este post, englobaremos tooooodo lo que incluye cada mini-algoritmo en el tiempo $$t$$ que toma preparar cada platillo, lo que simplifica el juego porque eso significa que, ahora, cada chef puede trabajar en uno y sólo un platillo a la vez.

Para poder pasar cada nivel, buscaremos la forma de preparar todos los platillos en el menor tiempo posible $$T$$. Es decir, queremos **minimizar** el tiempo que nos tomaría preparar todos los $$N$$ platillos al repartirlos entre los $$m$$ chefs del equipo.

Dos ejemplos rápidos para que quede claro (🚨 esto es súper importante para poder entender lo que sigue 🚨) antes de pasar a la parte de computación cuántica.

## Ejemplo #1

Si tenemos sólo $$m=1$$ chef y $$N=5$$ platillos donde sus tiempos están dados por:

$$ dishes = \{2, 3, 7, 2, 1 \} $$

Entonces la única opción es que ese chef prepare todos los platillos él mismo, así que el menor tiempo posible en que podemos terminar todas las órdenes es la suma del tiempo de cada una $$ T = 2+3+7+2+1 = 15$$.

## Ejemplo #2

Si ahora tenemos $$m=3$$ chefs para preparar los siguientes $$N=5$$ platillos:

$$ dishes = \{ 2,3,2,2,1 \} $$

Entonces (pueden hacerlo en una hoja de papel si quieren convencerse), el menor tiempo posible en que podemos terminar todas las órdenes será $$T=4$$, pero hay más de una forma de hacerlo. Por ejemplo, si $$m_i$$ es la lista de platillos que preparará el chef $$i$$. una forma sería:

$$m_1 = \{3\}, \quad m_2=\{2,2\}, \quad m_3=\{2,1\} $$

Mientras que otra opción sería:

$$m_1 = \{3,1\}, \quad m_2=\{2,2\}, \quad m_3=\{2\} $$

Ahora que ya entendimos el problema, viene la parte interesante: ¿cómo lo traducimos a un problema de Quantum Annealing?

## De la cocina a la cuántica

Como en todo problema de programación, hay varias formas de plantear un mismo problema y todas son correctas, pero para este caso, el [segundo ejemplo](#ejemplo-2) es el que sirve de motivación:

Si definimos el tiempo total que toma preparar cada lista $$m_i$$ como $$time(m_i)$$, podemos notar que una vez que se ha asignado la **lista óptima** $$m_{optimal}$$ (es decir, la lista de platillos que cumple $$time(m_{optimal})=T$$), el resto de los chefs pueden ser asignados con cualquier combinación de los platillos restantes y todas ellas son válidas siempre y cuando sus listas cumplan con la condición $$ time(m_i) \leq T$$ (porque así definimos a $$m_{optimal}$$).

En el [ejemplo 2](#ejemplo-2), el **chef óptimo** (es decir, el que fue asignado con la lista $$m_{optimal}$$) fue siempre el chef 2, pero en realidad no hay razón para decir que el segundo chef debe ser el que resuelva $$m_{optimal}$$ (es decir, todos los chefs son indistinguibles), así que podemos escoger al chef que queramos como el **chef óptimo** (a partir de ahora, escogeremos a $$m_1$$) y trataremos de minimizar su tiempo de preparación de acuerdo a las reglas del juego (condición 1) estableciendo la condición 2 para asegurarnos que en efecto el chef 1 será el **chef óptimo**:

1. Todos los platillos deben ser preparados exactamente una vez. Es decir, ningún chef estuvo trabajando en algún platillo diferente al mismo tiempo y, al final, no habrá ningún platillo que nos haya faltado por preparar.
2. El tiempo que le toma al chef 1 (el **chef óptimo**) preparar todos sus platillos da tiempo suficiente para que el resto de los chefs también preparen sus platillos:

$$ time(m_1) = T  \geq time(m_i) \quad \text{donde} \quad i \neq 1 $$

Como en computación cuántica necesitamos describir a los estados de nuestro sistema como una superposición de números binarios llamados **qubits** (si no lo recuerdan, pueden ir a ver [la entrada de Quantum Annealing](/posts/quantum_annealing/) en donde, de hecho, ya puse la solución a este problema 😉), vamos a utilizar **codificación unaria**. Es decir, la lista de platillos asignados a cada chef estará dada por un estado de $$N$$ qubits (un qubit para cada posible platillo) donde el qubit $$i$$ estará encendido $$\ket{1}$$ si le fue asignado a ese chef, y apagado $$\ket{0}$$ en caso contrario.

Por ejemplo, si el chef 1 preparó sólo el primer y el tercer platillo de 5 posibles:

$$\ket{m_1} = \ket{10100}$$

Así que el estado del sistema cuántico total (le llamaremos $$\ket{\psi}$$), estará conformado por los $$m$$ estados de los $$m$$ chefs (formalmente a esto se le conoce como el producto tensorial y, para los math geeks, omitiré el símbolo $$\otimes$$ por claridad):

$$\ket{\psi} = \ket{m_1} \ket{m_2} ... \ket{m_m} $$

Para encontrar la solución óptima para $$\ket{\psi}$$, necesitamos construir un Hamiltoniano (a.k.a "la función a minimizar") donde la energía (a.k.a "el valor a minimizar") represente el tiempo $$time(m_1)$$ sujeto a las dos condiciones anteriores.

![Quantum Overcooked](/assets/img/chefs/quantum_overcooked.jpg)
_Planteamiento del problema_

## El Hamiltoniano de Overcooked

Descompondremos la función a minimizar en tres partes.

Primero, queda claro que lo que queremos minimizar es el tiempo que le toma al **chef óptimo** preparar sus platillos. Como los platillos que preparará están codificados en qubits a modo de encendido/apagado, su tiempo estará dado sólo por los platillos que le tocó tener encendidos. Esto se puede representar fácilmente como el producto punto (la suma de los productos entrada a entrada) de dos vectores: el vector $$\vec{Q}$$ que representará la lista de posibles platillos y el vector $$\vec{m_1}$$ que es el que indicará los platillos a realizar:

{% include vector-eq.html src="/assets/img/chefs/cost_function.svg" width="100%" %}

Después, viene la primera condición que establece que cada platillo debe ser preparado una y sólo una vez. Las condiciones entrarán como multiplicadores de Lagrange [cómo también se mencionó en la entrada anterior](/posts/quantum_annealing/) y, en particular, esta puede escribirse como una condición de igualdad (por eso elevaremos al cuadrado) donde para cada platillo $$j$$, sólo un $$m_{ij}$$ debe estar encendido para todos los posibles valores de $$i$$:

{% include vector-eq.html src="/assets/img/chefs/condition_1.svg" width="80%" %}

Para la segunda condición que establece que el chef $$m_1$$ debe ser el **chef óptimo**