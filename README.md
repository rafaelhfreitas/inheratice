# composition, inheratice and multiple inheratice

Pratices of concepts compostion, inheritace and multipe inheritace

Creation of a HR system using [policy-based design](https://en.wikipedia.org/wiki/Modern_C%2B%2B_Design#Policy-based_design)

UML Diagram of application module composition:

![alt text](https://files.realpython.com/media/ic-policy-based-composition.6e78bdb5824f.jpg)

UML Diagram of application multiple_inheratice:

![alt text](https://files.realpython.com/media/ic-inheritance-policies.0a0de2d42a25.jpg)

Topics:

<ul>
    <li> Duck typing
    <li> Diamond Error with multiple inheratice using Python MRO to avoid this error
    <li> The classes explosion problem when utilize inheratice
    <li> What is better Composition or Inherit 
    <li> The type of relationships 'Is a' and 'Has a' 
    <li> When you should choose Composition or Inherit
    <li> Using mixin to add behavior for classes already implemented
    <li> Refactoring using factory pattern 
    <li> Refactoring using singleton pattern
</ul>

Resume when choose one design:

- Use inheritance over composition in Python to model a clear is a relationship. First, justify the relationship between the derived class and its base. Then, reverse the relationship and try to justify it. If you can justify the relationship in both directions, then you should not use inheritance between them.

- Use inheritance over composition in Python to leverage both the interface and implementation of the base class.

- Use inheritance over composition in Python to provide mixin features to several unrelated classes when there is only one implementation of that feature.

- Use composition over inheritance in Python to model a has a relationship that leverages the implementation of the component class.

- Use composition over inheritance in Python to create components that can be reused by multiple classes in your Python applications.

- Use composition over inheritance in Python to implement groups of behaviors and policies that can be applied interchangeably to other classes to customize their behavior.

- Use composition over inheritance in Python to enable run-time behavior changes without affecting existing classes.
