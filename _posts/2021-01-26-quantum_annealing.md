---
title: Quantum Annealing
date: 2021-01-26 13:00:00 +/-0600
categories: [Quantum Computing]
tags: [quantum-computing, optimization]
thumbnail: /assets/img/quantum-annealing/paper.png
math: true
---

# Introducción
Hoy vengo a compartirles una técnica que acabo de aprender que creo es una combinación muy bella y "simple" de varias cosas de física y programación. Ilustra muuuuy bien la promesa de la computación cuántica y se llama ["Quantum Annealing"](https://arxiv.org/abs/cond-mat/9804280).

![artículo de Quantum Annealing](/assets/img/quantum-annealing/paper.png)
_Quantum Annealing por T. Kadowaki y H. Nishimoro_

# La naturaleza y la cuántica 101
Primero, hay que recordar que la naturaleza es floja. Cualquier sistema, si se le deja evolucionar a su suerte, siempre buscará llegar al estado con menor energía posible gastando también la menor energía posible. Justo cómo el café que tiende a enfriarse y no a calentarse.

![Café enfriándose](/assets/img/quantum-annealing/coffee.jpeg)
_El café tiene menor energía cuando está frío que cuando está caliente_

¿Esto qué tiene que ver con la computación cuántica? Resulta que esto no sólo ocurre para sistemas "clásicos" como una taza de café, ¡sino que ocurre exactamente lo mismo en sistemas cuánticos!

No es necesario profundizar mucho, pero primero hay que recordar que las computadoras cuánticas funcionan a base de qubits en vez de bits. Un qubit es cualquier sistema (cuántico) que se pueda describir con dos estados. Uno de los ejemplos más simples es un electrón que puede ser un qubit a través de su spin que puede estar arriba :arrow_up: o abajo :arrow_down: .

Esto se hace en analogía con los dos estados de un bit (de hecho, a los dos estados del qubit se les llama $$\ket{0}$$ y $$\ket{1}$$), con la diferencia de que tenemos el poder de la superposición cuántica. Es decir, los qubits pueden estar en 0 y 1 al mismo tiempo.

![¿Qué es un qubit?](/assets/img/quantum-annealing/qubit.png)
_¿Qué es un qubit? Imagen adaptada de [Volkswagen](https://www.volkswagenag.com/en/news/stories/2019/11/where-is-the-electron-and-how-many-of-them.html)_

Por ejemplo, si tienes 2 qubits, significa que tienes al mismo tiempo todos los $$2^2$$ estados posibles $$\ket{00},\ket{01},\ket{10},\ket{11}$$ y puedes hacer operaciones con todos ellos de una sola pasada y en mucho menor tiempo que con una computadora clásica que tendría que hacerlo uno por uno.

{% include youtube.html id='4ZBLSjF56S8' %}

# Ajá, pero ¿y entonces qué es quantum annealing?

Aquí es donde viene la magia. Si combinamos el poder de la superposición con el caracter flojo de la naturaleza, podemos codificar problemas de minimización a un sistema cuántico y dejar que la naturaleza lo resuelva por nosotros haciendo que el estado con menor energía sea nuestra solución.

En otras palabras, si tenemos $$2^N$$ estados posibles del cual nos interesa el más óptimo (ejemplo: de $$N=1000$$ rutas a tomar, ¿cuál me toma menos tiempo?) puedo codificar el problema en un sistema cuántico de tal forma que la energía represente al tiempo y dejar que la naturaleza solita encuentre el mínimo porque eso es lo que le gusta hacer. Además, como el sistema cuántico estará en superposición, no necesitaría revisar ruta por ruta sino que la naturaleza lo hará para todas las rutas al mismo tiempo.

Cómo lograr esto también tiene su belleza y mucha física metida y hacer ingeniería con eso es la parte bonita de la computación cuántica.

Los sistema de spines de electrones ya los tenemos bien estudiados (le llamamos "Modelo de Ising") y conocemos la ecuación para calcular su energía (le llamamos "el Hamiltoniano"), así que sólo falta codificar el problema en términos de qubits. Aquí habrán algunas ecuaciones y no se preocupen si no las entienden, son para los math geeks o a los que les guste.

{% include vector-eq.html src="/assets/img/quantum-annealing/hamiltonian_spins.svg" width="80%" %}

Esto ya depende de cada problema, pero en el paper ["Ising formulations of many NP problems"](https://arxiv.org/pdf/1302.5843.pdf) hay 27 páginas de ejemplos y ya abordaré uno más a detalle en un artículo posterior. Lo importante para conjuntar esto con la progrmación es que los modelos de Ising se pueden ver como grafos (que es otra forma de llamarle a las "redes" y que están muy bien estudiados en computación) y son bien conocidos como problemas NP-Completos en el campo de programación lineal.

Como breviario cultural, en el argot de ciencias de la computación, los problemas:
- NP: son de decisión difíciles de resolver, pero fáciles de verificar.
- NP-Completos: son tal que pueden representar a **cualquier otro** de NP.
- NP-Difíciles: no son de decisión (pueden ser de optimización, por ejemplo), pero tan difíciles como los NP.

En general, cualquier problema de optimización lo podemos pasar a uno de decisión si en vez de preguntar "¿cuál es el valor mínimo/máximo?", preguntamos "¿existe algún valor menor/mayor que $$X$$?". ¡Ahí está la importancia! ¡Casi cualquier problema lo podemos resolver con un modelo de Ising!

Las condiciones que definen a un problema las podemos meter al Hamiltoniano de Ising con multiplicadores de Lagrange (les resultará familiar a los que ya hayan trabajado con problemas de optimización pero, si no, no se preocupen. De nuevo, es para los math geeks) de tal forma que la energía mínima se dé cuando nuestra función objetivo sea minimizada y no hayan restricciones violadas.

{% include vector-eq.html src="/assets/img/quantum-annealing/hamiltonian_multipliers.svg" width="100%" %}

Traducir eso a algo físico depende de cómo esté construida la computadora cuántica (puede ser con superconductores diminutos y campos magnéticos para manipular el spin), pero todos tienen algo en coḿun: la preparación del sistema. Ahí es donde entra el "annealing".

![Superconductores](/assets/img/quantum-annealing/superconductors.jpg)
_¿Cómo se ve un qubit?_

Si encendemos la computadora y enfriamos a los super conductores para que exhiban propiedades cuánticas, los estaríamos poniendo en su estado de energía mínima (se le llama "estado base"). ¡Pero lo que nos interesa es el estado base de NUESTRO sistema (con todo y restricciones)!

Físicamente, esta transformación se hace apagando los campos magnéticos que bootearon a la computadora gradualmente e ir encendiendo a los que van a configurar a nuestro sistema a un ritmo similar para, poco a poco, llevar a la computadora cuántica al sistema que nos interesa.

![Annealing](/assets/img/quantum-annealing/annealing.png)
_Qué sucede mientras pasa el annealing_

Este proceso se tiene que hacer muuuy despacio (en el argot físico se le llama "adiabáticamente") para que el estado base del sistema inicial se convierta en el estado base de nuestro sistema (que recordemos es la solución) con la menor cantidad de ruido posible.

![Proceso adiabático cuántico](/assets/img/quantum-annealing/adiabatic.png)
_Como el proceso es adiabático, el estado evoluciona del estado base del boot al estado base de nuestro sistema_

El ruido siempre es malo jajaja en este caso, lo es porque parte de su energía se le puede transferir a nuestros qubits y pasarían del estado base a algún estado excitado que pues ese NO es la solución que queremos!

Como en cuántica todo es probabilístico, el estado base será el que casi siempre observemos, pero pueden haber más. Sólo hay que ejecutar el programa varias veces hasta poder claramente discernir cuál aparece más y decir que ese es el base.

![Histograma](/assets/img/quantum-annealing/histogram.png)
_Histograma_

¡Y ya! :D Lo malo es que como el proceso debe ser adiabático, deberíamos ejecutarlo infinitamente despacio (literalmente) para obtener una solución 100% correcta. Hay algoritmos más nuevos (QAOA es súper state-of-art) que ofrecen un trade-off, pero eso será para otro hilo...