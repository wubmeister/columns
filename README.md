# Columns!

So, every site needs them, there is no real semantic way to use them responsively and it's a pain to write the code each time you need it. So here they are. Columns!

## Installation

You can just use the compiled `columns.css` out of the box. If, however, you need to do some customization, you can edit the variables in `colconfig.py` to accomodate your needs. Just copy colconfig.example.py to colconfig.py and start editing.

| Option       | Default value | Description                                                  |
| ------------ | ------------- | ------------------------------------------------------------ |
| breakpointSm | 576           | The width at which smablets start                            |
| breakpointMd | 768           | The width at which tablets start                             |
| breakpointLg | 992           | The width at which desktops start                            |
| breakpointXl | 1200          | The width at which wide screens start                        |
| padding      | 10            | Smallest padding for padded columns                          |
| paddingMore  | 20            | Medium padding for padded columns                            |
| paddingMost  | 40            | Large padding for padded columns                             |
| dividerSize  | 1             | Width of the dividers                                        |
| dividerColor | "#EBEBEB"     | Color of the dividers                                        |
| minify       | True          | True to minify the output CSS, False to produce readable CSS |

Then run `columns.py` to generate the CSS:

```sh
python3 columns.py
```

Once you have the `columns.css` that you want, you can include it in your HTML or CSS like you normally do:

```html
<link rel="stylesheet" type="text/css" href="columns.css" />
```

or

```css
@import url("columns.css");
```

## Usage

Check out the `examples.html` for the most common uses.

Columns need a container, with class `cols`. The columns should be direct descendants of that container and have the class `col`.

```html
<div class="cols">
    <div class="col">...</div>
    <div class="col">...</div>
    <div class="col">...</div>
    ...
</div>
```

Basically, there are three ways to divide your columns:

### Evenly divided columns

By using the class `cols-auto` on your container, all the columns will be evenly divided. This means that if you have two columns, they both will be 50% wide, if you have three columns, they all will be 33.33% wide and so on.

```html
<div class="cols cols-auto">
    <div class="col">This is a column</div>
    <div class="col">This is a column</div>
    <div class="col">This is a column</div>
    <div class="col">This is a column</div>
</div>
```

### Specifying the number of columns

This will also evenly divide the columns, but will give them a fixed with. Columns which don't fit on the same row will be pushed down to the next row.

```html
<div class="cols cols-2">
    <div class="col">This is a column</div>
    <div class="col">This is a column</div>
    <div class="col">This is a column on the second row</div>
    <div class="col">This is a column on the second row</div>
</div>
```

### Specifying the width per column

Assuming a base 'grid' of 12 columns, you can specify how many of those 12 columns one column should span. This means that `col-3` will span 3 columns, which will make it 25% wide.

```html
<div class="cols">
    <div class="col col-3">This is a 25% wide column</div>
    <div class="col col-3">This is a 25% wide column</div>
    <div class="col col-6">This is a 50% wide column</div>
</div>
```

To take this one step further, you can set the base 'grid' by specifying the number of columns in the container. The example below sets the base grid to 6 columns.

```html
<div class="cols-6">
    <div class="col col-2">This is a 33.33% wide column</div>
    <div class="col">This is a 16.67% wide column</div>
    <div class="col col-3">This is a 50% wide column</div>
</div>
```

## Padding

You can pad your columns whilst aligning them to the left and right side of the parent element. You can have three levels of padding: normal, more and most.

```html
<div class="cols cols-pad">
    <div class="col">...</div>
    <div class="col">...</div>
    <div class="col">...</div>
</div>
```

More padding:

```html
<div class="cols cols-pad-more">
    <div class="col">...</div>
    <div class="col">...</div>
    <div class="col">...</div>
</div>
```

Most padding:

```html
<div class="cols cols-pad-most">
    <div class="col">...</div>
    <div class="col">...</div>
    <div class="col">...</div>
</div>
```

## Grid

A grid with padding has - besides horizontal padding - also vertical padding. Use the class `cols-grid` on the container to get the grid effect.

The following code produces a 2x2 padded grid:

```html
<div class="cols cols-grid cols-2 cols-pad">
    <div class="col">...</div>
    <div class="col">...</div>
    <div class="col">...</div>
    <div class="col">...</div>
</div>
```

## Dividing

You can divide your columns with a nice border. This combines well with (but is not restricted to) padded columns. To use this, just add the `cols-divide` class to your container.

```html
<div class="cols cols-divide">
    <div class="col">...</div>
    <div class="col">...</div>
    <div class="col">...</div>
</div>
```

## Alignment

It is possible to align columns inside the container, by using the `cols-left`, `cols-right`, `cols-center` and `cols-justify` classes on the `cols` container.

You can also align the text inside a column by using the `col-left`, `col-right` and `col-center` classes on the column


## Responsive

Almost all classes can have breakpoint specifiers, to specify from which breakpoint on up the effects of that class should be visible.

If the original class name is `cols-*`, then you can use `cols-sm-*` to use this for smablets and up, `cols-md-*` for tablets and up, `cols-lg-*` for desktops and up and `cols-xl-*` for wide screens. The same works for `col-*`.

For example, this setup will render 2 columns on small devices and 4 columns on tablets, desktops and wide screens:

```html
<div class="cols cols-2 cols-md-4">...</div>
```

And this code will render a column to span 4 base grid columns on small devices and tablets and 4 base columns on desktops and wide screens:

```html
<div class="col col-4 cols-lg-2">...</div>
```

## All the classes

Below you can find a table with all the class names. When you see `[1-12]` in the class name, it means that there comes a number bewtween 1 and 12. When you see `[sm,md,lg,xl]`, it that there comes a responsive modifier: `sm`, `md`, `lg` or `xl`.

### For column containers

| Class name                   | Responsive class name                      | What it does                                                                         |
| ---------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------ |
| <nobr>`cols`</nobr>          |                                            | Defines a column container. Column containers MUST all have this class name.         |
| <nobr>`cols-auto`</nobr>     | <nobr>`cols-[sm,md,lg,xl]-auto`</nobr>     | Tells the browser to size the columns evenly                                         |
| <nobr>`cols-[2-12]`</nobr>   | <nobr>`cols-[sm,md,lg,xl]-[2-12]`</nobr>   | Specifies the number of columns or the base grid.                                    |
| <nobr>`cols-pad`</nobr>      | <nobr>`cols-[sm,md,lg,xl]-pad`</nobr>      | Pads the columns slightly.                                                           |
| <nobr>`cols-pad-more`</nobr> | <nobr>`cols-[sm,md,lg,xl]-pad-more`</nobr> | Pads the columns some more.                                                          |
| <nobr>`cols-pad-most`</nobr> | <nobr>`cols-[sm,md,lg,xl]-pad-most`</nobr> | Pads the columns even more.                                                          |
| <nobr>`cols-divide`</nobr>   | <nobr>`cols-[sm,md,lg,xl]-divide`</nobr>   | Divides the columns with a line                                                      |
| <nobr>`cols-left`</nobr>     | <nobr>`cols-[sm,md,lg,xl]-left`</nobr>     | Pushes all the columns to the left side of the container. This is default behaviour. |
| <nobr>`cols-center`</nobr>   | <nobr>`cols-[sm,md,lg,xl]-center`</nobr>   | Places all the columns in the horizontal middle of the container.                    |
| <nobr>`cols-right`</nobr>    | <nobr>`cols-[sm,md,lg,xl]-right`</nobr>    | Pushes all the columns to the right side of the container.                           |
| <nobr>`cols-justify`</nobr>  | <nobr>`cols-[sm,md,lg,xl]-justify`</nobr>  | Spreads the columns over the column so that the first one is all the way on the left and the last one is all the way on the right |

### For columns

| Class name                | Responsive class name                   | What it does                                                 |
| ------------------------- | --------------------------------------- | ------------------------------------------------------------ |
| <nobr>`col`</nobr>        |                                         | Defines a column. Columns MUST all have this class name.     |
| <nobr>`col-[2-12]`</nobr> | <nobr>`col-[sm,md,lg,xl]-[2-12]`</nobr> | Specifies how many base gris columns this column should span |
| <nobr>`col-left`</nobr>   | <nobr>`col-[sm,md,lg,xl]-left`</nobr>   | Left aligns the text in the column                           |
| <nobr>`col-center`</nobr> | <nobr>`col-[sm,md,lg,xl]-center`</nobr> | Centers the text in the column                               |
| <nobr>`col-right`</nobr>  | <nobr>`col-[sm,md,lg,xl]-right`</nobr>  | Right aligns the text in the column                          |
