# CP1404 Practical Reflection

Write short but thoughtful answers to each of the following.  
Replace each `...` with your meaningful answer.

## Estimates

Regarding the **estimates** that you did for practical tasks...

### How was your estimate accuracy usually?

Usually it was around 40%

### How did your estimate accuracy improve or change during the course of the subject?

I will try to be affluent in my knowledge and ask the classmate, teacher. 

### What did you learn from doing these estimates?

Familiarity with the problems 

## Code Reviews

### What have you learned from being reviewed by other people?

What they did is pretty different then what I have done. They give me a lot of new idea 
for coding. 

### What have you learned from doing code reviews of other people?

I had compare others, I had learn different way to type the code.

Provide proper Markdown links (not bare URLs) to two (2) PRs that show you doing good code reviews for any of the past
pracs.  
For each one, write a short explanation of what was good about your review.

### Good Code Review 1

[from kivy.app import App
 from kivy.uix.widget import Widget
 from kivy.graphics import Color, Rectangle, Ellipse
 
 
 class BasicGraphicsDemo(App):
     def build(self):
         self.root = Widget()
 
         # white rectangle 100x100
         self.root.canvas.add(Color(1, 1, 1, 1))
         self.root.canvas.add(Rectangle(size=(100, 100)))
 
         # blue circle 50x50
         self.root.canvas.add(Color(0, 0, 1, 1))
         self.root.canvas.add(Ellipse(size=(50, 50), pos=(50, 50)))
         return self.root
 
 
 BasicGraphicsDemo().run()](KennardLim)

### Explanation

He has made a class for this programming. 

### Good Code Review 2

[from kivy.app import App
 from kivy.lang import Builder
 
 
 class AnchorLayoutDemo(App):
     def build(self):
         self.title = "Anchor Layout Demo"
         self.root = Builder.load_file('anchor_layout.kv')
         return self.root
 
 
 # create and start the App running
 AnchorLayoutDemo().run()](KennardLim)

### Explanation

Nice and clear for the program.

## Practicals

### Regarding the **practical tasks** overall, what would you change if you were in charge of the subject?

Well, I think it is pretty well for now. However, I think I can make the website more easier to read. 

### What did you do really well for practicals in this subject?

I always turn in the homework ontime and will learn the coding with others. 
