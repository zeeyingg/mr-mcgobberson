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
- Creating and linking CSS style sheet
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



### Resources
* thing1
* thing2

---

Accurate as of (last update): 2022-10-21

#### Contributors:  
Ziying Jian, pd2  
Talia Hsia, pd2  
Jasmine Yuen, pd2   
