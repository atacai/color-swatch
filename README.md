# Colors Swatches

1. Random color in 5 set every API called. Total set can be configured from Django `settings.py` file with field `DEFAULT_SWATCHES_SET`.

1. Added models to configure color:
    * `Color`
        * `name`: CharField, name of color set, example: rgb, hsl. This name also will be used to generate color in frontend, example: `rgb()`, `hsl()`
    * `Range`
        * `name`: CharField, name of color range, example: red, hue
        * `range_start`: IntegerField, start point for color range, example red is 0, hue is 0
        * `range_stop`: IntegerField, end point for color range, example red is 255, hue is 360
        * `suffix`: CharField, unit for color range. This field is not required to fill in, example saturation is %
        * `color`: ForeignKey, relation field to `Color` model.

1. Registered `Color` and `Range` model in admin site. To add new set for color set, we can go to admin site to add, example like adding BRGB on **Stage 2**

1. Fixtures available for `rgb` and `hsl` data in `colors/fixtures/data.json`. We can load data using `loaddata` command.