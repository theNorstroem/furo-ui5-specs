name: BytesValue
type: BytesValue
description: |-
    Wrapper message for `bytes`.

     The JSON representation for `BytesValue` is JSON string.
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
        type: bytes
        description: The bytes value.
        __proto:
            number: 1
        __ui: null
        meta:
            default: ""
            placeholder: ""
            hint: ""
            label: label.BytesValue.value
            options:
                flags: []
                list: []
            readonly: false
            repeated: false
            typespecific: null
        constraints: {}
