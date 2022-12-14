name: UInt64Value
type: UInt64Value
description: |-
    Wrapper message for `uint64`.

     The JSON representation for `UInt64Value` is JSON string.
lifecycle: null
__proto:
    package: google.protobuf
    targetfile: wrappers.proto
    imports: []
    options:
        csharp_namespace: Google.Protobuf.WellKnownTypes
        go_package: google.golang.org/protobuf/types/known/wrapperspb
        java_multiple_files: "true"
        java_outer_classname: WrappersProto
        java_package: com.google.protobuf
        objc_class_prefix: GPB
fields:
    value:
        type: uint64
        description: The uint64 value.
        __proto:
            number: 1
        __ui: null
        meta:
            default: ""
            placeholder: ""
            hint: ""
            label: label.UInt64Value.value
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
