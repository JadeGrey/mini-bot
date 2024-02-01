#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import wpilib.drive


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        backLeftMotor = wpilib.PWMSparkMax(0)
        backRightMotor = wpilib.PWMSparkMax(2)
        frontLeftMotor = wpilib.PWMSparkMax(1)
        frontRightMotor = wpilib.PWMSparkMax(3)
        self.backRobotDrive = wpilib.drive.DifferentialDrive(backLeftMotor, backRightMotor)
        self.frontRobotDrive = wpilib.drive.DifferentialDrive(frontLeftMotor, frontRightMotor)
        self.stick = wpilib.Joystick(0)
        backRightMotor.setInverted(True)
        frontRightMotor.setInverted(True)

    def teleopPeriodic(self):
        self.backRobotDrive.arcadeDrive(self.stick.getY(), self.stick.getX())
        self.frontRobotDrive.arcadeDrive(self.stick.getY(), self.stick.getX())