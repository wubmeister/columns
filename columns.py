import colconfig

width_selectors = dict()
file = open("columns.css", "w")
minify = colconfig.minify

def block_start(prelude, indent = ""):
    if minify:
        prelude = prelude.replace(" > ", ">").replace(" + ", "+").replace(": ", ":").replace(", ", ",")
    elif indent != "":
        file.write(indent)
    file.write(prelude)
    if minify == False:
        file.write(" {\n")
    else:
        file.write("{")

def block_end(indent = ""):
    if minify == False:
        file.write("%s}\n" % indent)
    else:
        file.write("}")

def write_prop(prop, value, indent = ""):
    if minify == False:
        file.write("%s  " % indent)
    file.write(prop)
    if minify == False:
        file.write(": ")
    else:
        file.write(":")
    file.write(value + ";")
    if minify == False:
        file.write("\n")

def add_width_selector(width, selector):
    key = "%f" % width
    key = key.replace(".000000", "")
    if key not in width_selectors:
        width_selectors[key] = []
    width_selectors[key].append(selector)

def spans(prefix, base = 12):
    for num in range(2,base):
        width = 100.0 * num / base
        add_width_selector(width, ".cols-%s%d > .col-%d" % (prefix,base,num))
        if prefix != "":
            add_width_selector(width, ".cols-%d > .col-%s%d" % (base,prefix,num))

def basespans(prefix):
    for num in range(2,12):
        width = 100.0 * num / 12
        add_width_selector(width, ".cols > .col-%s%d" % (prefix,num))

def columns(prefix = ""):
    basespans(prefix)
    for num in range(2,12):
        width = 100.0 / num
        add_width_selector(width, ".cols-%s%d > .col" % (prefix,num))
        spans(prefix, num)

def padding(indent, prefix, postfix, padding):
    block_start(".cols-%spad%s" % (prefix,postfix), indent)
    write_prop("margin", "0 -%dpx" % (padding), indent)
    block_end(indent)
    block_start(".cols-%spad%s > .col" % (prefix,postfix), indent)
    write_prop("padding", "0 %dpx" % (padding), indent)
    block_end(indent)

def breakpoint(prefix = "", min_width = 0):
    width_selectors.clear()

    columns(prefix)

    indent = ""
    joiner = ", " if minify == False else ","

    if prefix:
        block_start("@media screen and (min-width: %dpx)" % (min_width))
        indent = "  " if minify == False else ""

    for width in width_selectors:
        block_start(joiner.join(width_selectors[width]), indent)
        write_prop("width", "%s%%" % width)
        block_end(indent)

    padding(indent, prefix, "", colconfig.padding)
    padding(indent, prefix, "-more", colconfig.paddingMore)
    padding(indent, prefix, "-most", colconfig.paddingMost)

    block_start(".cols-%sdivide > .col + .col" % (prefix), indent)
    write_prop("border-left", "%dpx solid %s" % (colconfig.dividerSize,colconfig.dividerColor), indent)
    block_end(indent)
    block_start(".cols-%sleft" % (prefix))
    write_prop("justify-content", "flex-start", indent)
    block_end(indent)
    block_start(".cols-%scenter" % (prefix))
    write_prop("justify-content", "center", indent)
    block_end(indent)
    block_start(".cols-%sright" % (prefix))
    write_prop("justify-content", "flex-end", indent)
    block_end(indent)
    block_start(".cols-%sjustify" % (prefix))
    write_prop("justify-content", "space-between", indent)
    block_end(indent)

    if prefix:
        block_end()

block_start(".cols, .cols > .col")
write_prop("box-sizing", "border-box")
block_end()
block_start(".cols")
write_prop("display", "flex")
write_prop("flex-wrap", "wrap")
write_prop("margin", "0")
block_end()
block_start(".cols-auto")
write_prop("justify-content", "space-evenly")
write_prop("flex-wrap", "nowrap")
block_end()
block_start(".cols > .col")
write_prop("width", "100%")
write_prop("padding", "0")
block_end()

breakpoint()
breakpoint("sm-", colconfig.breakpointSm)
breakpoint("md-", colconfig.breakpointMd)
breakpoint("lg-", colconfig.breakpointLg)
breakpoint("xl-", colconfig.breakpointXl)
