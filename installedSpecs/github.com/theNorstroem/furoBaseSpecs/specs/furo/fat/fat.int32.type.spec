name: Int32
type: Int32
description: Furo annotated type wrapper message for `int32`.
lifecycle: null
__proto:
    package: furo.fat
    targetfile: fat.proto
    imports: []
    options:
        csharp_namespace: Furo.Fat
        go_package: github.com/theNorstroem/FuroBaseSpecs/dist/pb/furo/fat;fatpb
        java_multiple_files: "true"
        java_outer_classname: FatProto
        java_package: pro.furo.fat
        objc_class_prefix: FAT
fields:
    value:
        type: int32
        description: The JSON representation for `Int32Value` is JSON number
        __proto:
            number: 1
        __ui:
            component: ""
            flags: []
            noinit: false
            noskip: false
        meta:
            default: ""
            placeholder: ""
            hint: ""
            label: ""
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    labels:
        type: map<string,bool>
        description: Labels / flags for the value, something like unspecified, empty, confidential, absent,... Can be used for AI, UI, Business Logic,...
        __proto:
            number: 2
        __ui:
            component: ""
            flags: []
            noinit: false
            noskip: false
        meta:
            default: ""
            placeholder: ""
            hint: ""
            label: ""
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
    attributes:
        type: map<string,string>
        description: 'Attributes for a value, something like confidential-msg: you are not allowed to see this value'
        __proto:
            number: 3
        __ui:
            component: ""
            flags: []
            noinit: false
            noskip: false
        meta:
            default: ""
            placeholder: ""
            hint: ""
            label: ""
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
