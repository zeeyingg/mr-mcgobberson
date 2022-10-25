# how-to :: CSS FLEXBOX CONTAINERS
---
## Overview
Flexboxes, or Flexible Box Layout Model, is designed to group items into one container to allow for it to be easily displayed on a page.

Particularly, it becomes much easier when you're able to provide attributes that describe how each container and their children should size themselves, wrap or align content, and how much spacing should be applied.

For instance, with Flexbox, it's easy to create a layout that is fixed to the height of the browser window and adjusts all panels when the browser resizes. You can easily control the wrapping behavior, making it easier to create responsive and mobile-friendly layouts.

### Estimated Time Cost: x.x hrs (round to nearest 0.1)

### Prerequisites:
- Know HTML basic syntax
- Creating <div> classes
- Creating and linking CSS code (whether through internal or external style sheet)
- Have Chrome, Edge, Firefox, Safari, or Opera installed

1. To create a flex container:
```HTML
<div class="container" id="container">
  <div>Item One</div>
  <div>Item two</div>
  <div>The item we will refer to as three</div>
</div>
```
Here's what it looks like:
![flexbox diagram](https://miro.medium.com/max/1183/1*ubDrM-3m22gLF_pZ4DCdMw.png)

2. Declare flex formatting context, not regular block and lineline layout using CSS.
```CSS
.container {
  display: flex;
}
```

### Flex-Box Properties:

#### Flex-direction:
Flex-direction sets the direction that each subsequent item is placed relative to the previous ones in a flex box. For example, if the flex-driection was set to column then the items would be placed starting at the top and each item after would be placed below it. 

CSS flex direction attribute:
```CSS
.container{
  display: flex;
  flex-direction: row | row-reverse | column | column-reverse;
}
```

Possible flex-direction settings are 
- row: goes left to right (default)
- row-reverse: goes right to left
- column: goes top to bottom
- column-reverse: goes bottom to top


#### Flex-wrap:

Flex-wrap handles item layout when it exceeds the amount that can fit on one line by allowing it to wrap onto the next line.

CSS flex-wrap attribute:
```CSS
.container{
  display: flex;
  flex-wrap: wrap | nowrap | wrap-reverse;
}
```

Possible flex-wrap settings are
- wrap: items will wrap onto the next line when needed
- nowrap: items will all remain on one line (default)
- wrap-reverse: items start on the bottom and wrap towards the line above it


#### Flex-flow

Flex-flow combines flex-wrap and flex-direction into one property. This requires specifying both the direction and wrap setting in the attribute. This can be any combination of a flex direciton setting and then a wrap setting which are separated by a space. By default, the flex-flow is set to row and nowrap.

Here's an example:
```CSS
.container{
  display: flex;
  flex-flow: row-reverse wrap;
}
```

### To learn more about flex boxes and their properties:
* https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox
* https://www.w3schools.com/css/css3_flexbox_container.asp

---

Accurate as of (last update): 2022-10-21

#### Contributors:  
Ziying Jian, pd2  
Talia Hsia, pd2  
Jasmine Yuen, pd2   
