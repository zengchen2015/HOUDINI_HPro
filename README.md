# HOUDINI_HPro

- The document :  [<u>Yuque Web</u>](https://www.yuque.com/zengchen2020/hpro_help)
- The example hips :  [<u>HIP on Github</u>](https://github.com/zengchen2015/HOUDINI_HPro_HIP)

---

Some of my HDAs are not useful now in Houdini v18.5. You can modify the **OPcustomize** file to hide the specified HDA in TAB menu. But do not delete them, because some of them may wrapped by other HDAs.

The command pattern is `ophide Network OperatorName`

For example : 

- You can write the follow statement in the **OPcustomize** file to hide my Assemble HDA : 

    ```
    ophide Sop hpro::simple_assemble
    ```

    - `Sop` : my Assemble HDA is in the Sop network
    - `hpro::simple_assemble` : my Assemble HDA's operator name (operator type).

- And you can add `//` prefix to disable a statement 

    ```
    // ophide Sop hpro::simple_assemble
    ```

    In this way, the "ophide" command will be disabled.

---

Here are the HDAs I highly recommend you to use (which satisfied me when complete those HDAs ) :

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

