
Motivation
###########

Thinking about how you work to improve your efficiency is an effort, and it requires to challenge yourself from time to time. In my own experience, people may consider that it is a waste of time, and doing it the *quick and dirty way* is enough. Or they already know one method to accomplish a task that is enough for them, and they want to stick with it. In the short term, it is definitely faster, but I think taking the time to improve your workflow always proves worthwhile, at least in the mid-long term.

For sure, I can testify that during my PhD thesis, it allowed me to go further in my research, more than I could without trying to look for better tools to help me in my work. Without even talking about computer tools, just thinking about the way you can improve your workflow is already a great start! Challenge your habits, try to see where you spend the most time, and look around how people do it.

A simple example
----------------

When I was an undergraduate student in applied mathematics, I was always spending a lot of time, not just producing data for my numerical experiments, but post-processing them (organizing the data files, plotting the output, ...). At the time, I was more focused on the core of my work, which was solving a partial differential equation. So I did not want to spend too much time on “technical details”, and ironically, I was...

It came to a point where it was ridiculous, and something needed to be done. Like some students, I had one executable/script doing everything (computations like solving a linear system, analyses like doing a linear regression, plots, ...), and every parameter was hard coded. It was convenient (I thought) since I just had to push a button, and I had directly the results I wanted. But here are the **issues**:

- Surprisingly, nothing works the first time, and having everything in the same code makes you debug everything at the same time.
- The analysis you want to carry over your data is never relevant the first time, so you need to rerun everything each time you want to explore your data, in particular run computations which is the most expensive part.
- The first plots are always ugly, so you also need to rerun everything.
- In case of compiled code, you need to recompile each time you want to change some parameters.

My solution (that may seem obvious to you now, but remember, I was an undergraduate student at the time) consisted in formalizing my numerical experiment as a pipeline where each code component could be implemented separately and needed to take some inputs and create some outputs:

.. figure:: ../_static/svg/introduction/pipeline.drawio.svg
   :align: center
   
   Work pipeline

Obviously, it seems more complicated than doing everything in one code/script, and you need to manage inputs and outputs for each code component. But, it has several **advantages**:

- The fact that `Computation` takes `Input` as an argument makes you able to loop over the input parameters, and to generate more data with a simple script.
- If you have several pipelines with similar `Computation` component, you can try to merge them to make one pipeline, that takes more input to recover the exact previous computations.
- You can do as many analyses as you want on `Data`.
- Using well-know formats, such as `csv`, `json` or others (depending on your data) for `Input`, `Data` and `Output` makes you able to use most of the languages/software programs I/O utilities, post-processing and plotting tools. For example, you can easily use the python modules `pandas` and `matplotlib`, :math:`\LaTeX` package `pgfplot`, etc.
- You can save and store your results `Data` and `Output`.

Of course, you should not break your pipeline into too many components, there is a balance to be struck, and this was a very simple/naive example just to show you how changing your workflow actually allows you to **do more in your core work**. In this example, more computations with more inputs, and more analyses using more post-processing components.

Take home message
-----------------

It is very valuable to take the time to work on your workflow, even for your core work. Another reason is that you are very likely to learn new tools, and thus get new transferable skills that you will probably be able to use throughout your career. Besides, it is also very intellectually satisfying to see we can improve and to see the net profit we get in our daily work life.

The goal
--------

In this document, you will find several introductions to tools that can help you improve the way you code, from the most basic to more advanced. The focus will be more on what each tool can provide, I will not dwell upon all the installation procedures, but references to relevant documentations will be given. More generally, I will try to always give references for you to start looking out and go further. As I said earlier, a workflow is *personal*, and you need to make it your own. 
