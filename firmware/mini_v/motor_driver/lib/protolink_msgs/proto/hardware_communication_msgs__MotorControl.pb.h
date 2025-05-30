/* Automatically generated nanopb header */
/* Generated by nanopb-1.0.0-dev */

#ifndef PB_PROTOLINK__HARDWARE_COMMUNICATION_MSGS__MOTORCONTROL_PROTO_HARDWARE_COMMUNICATION_MSGS__MOTORCONTROL_PB_H_INCLUDED
#define PB_PROTOLINK__HARDWARE_COMMUNICATION_MSGS__MOTORCONTROL_PROTO_HARDWARE_COMMUNICATION_MSGS__MOTORCONTROL_PB_H_INCLUDED
#include <pb.h>

#if PB_PROTO_HEADER_VERSION != 40
#error Regenerate this file with the current version of nanopb generator.
#endif

/* Struct definitions */
typedef struct _protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl {
    bool motor_enable;
    double motor_speed;
    uint32_t mode;
} protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl;


#ifdef __cplusplus
extern "C" {
#endif

/* Initializer values for message structs */
#define protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_init_default {0, 0, 0}
#define protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_init_zero {0, 0, 0}

/* Field tags (for use in manual encoding/decoding) */
#define protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_motor_enable_tag 1
#define protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_motor_speed_tag 2
#define protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_mode_tag 3

/* Struct field encoding specification for nanopb */
#define protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, BOOL,     motor_enable,      1) \
X(a, STATIC,   SINGULAR, DOUBLE,   motor_speed,       2) \
X(a, STATIC,   SINGULAR, UINT32,   mode,              3)
#define protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_CALLBACK NULL
#define protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_DEFAULT NULL

extern const pb_msgdesc_t protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_msg;

/* Defines for backwards compatibility with code written before nanopb-0.4.0 */
#define protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_fields &protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_msg

/* Maximum encoded size of messages (where known) */
#define PROTOLINK__HARDWARE_COMMUNICATION_MSGS__MOTORCONTROL_PROTO_HARDWARE_COMMUNICATION_MSGS__MOTORCONTROL_PB_H_MAX_SIZE protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_size
#define protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_size 17

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif
