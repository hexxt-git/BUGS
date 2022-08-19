# introducrion
  2D creatures evolution simulator written in python.

# evolution
<ul>
<li>each generation all the creatures die and new ones are born from two parents.</li>
<li>only parents that pass the selection criteria get to reproduce.</li>
<li>the offspring inherint features randomly from one of the parents, some features can be mix from both.</li>
<li>features mutate on random occasions.</li>
</ul>

# creatures
these creatures can evolve brains for navigation and distinct colours to differentiate spieces and show diversity.

# brains
composed of connections from <b>inputs</b> to <b>outputs</b> with <b>weights</b> and <b>biases</b> that are all configurable and be evolved<br>
after all the inputs are set and outputa are calculated, the output with the heighest activation is activated

# selection
currently set to select parents only from the 8 eastern possition, teaching the species to travel east.
