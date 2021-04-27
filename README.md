# HOUDINI_HPro

- The document :  [<u>Yuque Web</u>](https://www.yuque.com/zengchen2020/hpro_help)
- The example hips :  [<u>HIP on Github</u>](https://github.com/zengchen2015/HOUDINI_HPro_HIP)

---

Some of my HDAs are not useful now in Houdini v18.5. You can modify the **OPcustomize** file to hide the specified HDA in TAB menu. But do not delete them, because some of them may wrapped by other HDAs.

The command pattern is `ophide Network OperatorName`

For example : 

- You can write the follow statement in the **OPcustomize** file to hide my HPro - Assemble HDA : 

    ```
    ophide Sop hpro::simple_assemble
    ```

    - `Sop` : my HPro - Assemble HDA is in the Sop network
    - `hpro::simple_assemble` : my HPro - Assemble HDA's operator name (operator type).

- And you can add `//` prefix to disable a statement 

    ```
    // ophide Sop hpro::simple_assemble
    ```

    In this way, the "ophide" command will be disabled.

---

Some HDAs need more improvement : 

- [ ] piece arrange : add "visualize piece attribute" feature.
- [ ] curve wire : consider to use "sweep" SOP to replace wrangle node that will be faster to create a wire, and use "sweep" SOP can custom the div num.
- [ ] curve wrap
    - simplify the copy source attributes feature
    - support the geo lib input
- [ ] sweep geometry : consider to use improved "curve wrap" HDA and "curve custom split" HDA inside to achieve the feature of "chain" SOP and will be much faster than "chain" SOP.

---

Here are the HDAs I highly recommend you to use (which satisfied me when complete these HDAs ) :

- boolean curve
- carve curve
- convert edge group to line
- copy groups by match attribute
- create detail attribute for loop
- curve even split
- curve frame
- get sorted id
- group by attribute
- piece arrange
- point orient
- quad scatter / quad scatter utility



