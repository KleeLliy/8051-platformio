#ifndef REG8052_H
#define REG8052_H

#include "8051.h"

// 定义8052单片机特殊功能寄存器

// T2CON
__sfr __at (0xC8) T2CON ;

// RCAP2L   // RCAP2H
__sfr __at (0xCA) RCAP2L  ;
__sfr __at (0xCB) RCAP2H  ;
__sfr __at (0xCC) TL2     ;
__sfr __at (0xCD) TH2     ;


// IE 
__sbit __at (0xAD) ET2    ; // 允许T2中断


// IP
__sbit __at (0xBD) PT2    ; // T2中断优先级标志位

// T2CON
__sbit __at (0xC8) T2CON_0 ;
__sbit __at (0xC9) T2CON_1 ;
__sbit __at (0xCA) T2CON_2 ;
__sbit __at (0xCB) T2CON_3 ;
__sbit __at (0xCC) T2CON_4 ;
__sbit __at (0xCD) T2CON_5 ;
__sbit __at (0xCE) T2CON_6 ;
__sbit __at (0xCF) T2CON_7 ;

// 其他标志
__sbit __at (0xC8) CP_RL2  ;
__sbit __at (0xC9) C_T2    ;
__sbit __at (0xCA) TR2     ;
__sbit __at (0xCB) EXEN2   ;
__sbit __at (0xCC) TCLK    ;
__sbit __at (0xCD) RCLK    ;
__sbit __at (0xCE) EXF2    ;
__sbit __at (0xCF) TF2     ;

#endif
