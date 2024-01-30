Submission: https://canvas.unf.edu/courses/100860/assignments/1328145

Libraries:

Tkinter



Installation:


Set-up Guide:
    Tkinter



Please include a README file describing what works and
what does not, the results of your experiments, any known bugs, and any problems you
encountered


<h1>Problems encountered</h1>

    1. I attempted to use the Qt C++ Library, but it became too unwieldly to implement.
        I would like to implement Qt and take advantage of C++, but from what I can tell it would need
    

<h1>Introduction</h1>
<h1>Project 1 – Exploring $-family recognizers</h1>
<h5>Due: 2/8/24 11:59 pm<h5/>

This project was created by John S. Reddick. The outline of the following project requirements are adapted from the 
    project description created by Corey Pittman in 2024. I have included an original copy of the instructions 
[here](.\SpecialTopicsProj1 "here")

<ol>
  <h2><li>Purpose</h2>
    The purpose of this assignment is twofold. It is first designed to give you experience with simple
    recognizers using reliable data (touch/stylus/mouse). Second, it is to give you experience with
    implementing a state of the art algorithms from scratch by relying on algorithms provided in
    the research paper
    </li>

  <h2><li>Requirements</h2>
    There are two main requirements for this assignment. First, you will implement 3 $- family
    recognizers and compare them.

Train each recognizer with 1, 3, and 5 samples per symbol. Test each recognizer by writing each
symbol 5 times, which should give you a good accuracy number. You should run separate
experiments using the data you collected using a mouse vs a touch screen (if applicable). Please
put the results of your experiment in your README file.
  </li>

  <h2><li>Recognizers</h2>
The first is the $N recognizer discussed here:
Anthony, L. and Wobbrock, J.O. (2010). A lightweight multistroke recognizer for user interface
prototypes. Proceedings of Graphics Interface (GI '10). Ottawa, Ontario (May 31-June 2, 2010).
Toronto, Ontario: Canadian Information Processing Society, pp. 245- 252.
The second recognizer is known as Protractor and details can be found here:

Li, Yang (2010). Protractor: a fast and accurate gesture recognizer. In Proceedings of the SIGCHI
Conference on Human Factors in Computing Systems (CHI '10). ACM, New York, NY, USA, 2169-
2172, April 2010.

The third recognizer is known as Penny Pincher and the details can be found here:
Taranta, E. and LaViola, J. Penny Pincher: A Blazing Fast, Highly Accurate $-Family Recognizer,
Proceedings of Graphics Interface 2015, 195-202, June 2015.
You should test these algorithms with the following symbols: 0,1,2,3,4,5,6,7,8,9,+,-,*,t,a,n,s,c,i,
and the square root symbol. I would also recommend adding some more oddball symbols of
your own choosing</li>

  <h2><li>Strategy</h2>
    The first step of this project is to create some kind of basic canvas drawing application. This can
    be done in any programming language of your choosing, though I recommend looking into the
    capabilities of C# with WPF, Python with TK, Java with Swing, or HTML/JS/CSS. No choice is
    inherently better than others. You will want to create buttons or widgets to enable the user to
    clear the canvas, trigger recognition, and undo previous written strokes. Please see
    https://www.eecs.ucf.edu/isuelab/demo/stochastic-resampling/ or
    https://depts.washington.edu/acelab/proj/dollar/index.html for examples of similar canvas
    implementations which you can work from. Reach out to the instructor if more examples are
    needed.
    </li>
  <h2><li>Implementation</h2>
To  your symbol recognizers, there are some things you need to consider.
1. You need to find a way to invoke the recognizer. You can have it run in real time or in
batch mode (by pressing a button or doing a different, heuristically determined gesture)

2. You will need to show recognition results to the user. A simple text box is fine but if you
want to be more elaborate feel free to do so.
    </li>
  <h2><li>Deliverables</h2>
Upload your source code to Canvas. Please include a README file describing what works and
what does not, the results of your experiments, any known bugs, and any problems you
encountered
    </li>
    <h2><li>Grading</h2>
    80% correct implementation of the recognizers
    20% documentation
    </li>
</ol>


