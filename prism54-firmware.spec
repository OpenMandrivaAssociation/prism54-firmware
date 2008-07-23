%define name prism54-firmware
%define version 1.0.4.3
%define isl3877_version 1.1.0.0
%define release %mkrel 3

Summary: Firmware for the Linux prism54 driver
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prism54.org/firmware/%{version}.arm
Source1: http://prism54.org/firmware/%{isl3877_version}.arm
License: Maybe redistributable
Group: System/Kernel and hardware
Url: http://prism54.org/fullmac.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch


%description
Firmware for the Linux Kernel prism54 driver.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib/firmware
install %{SOURCE0} $RPM_BUILD_ROOT/lib/firmware/isl3890
install %{SOURCE1} $RPM_BUILD_ROOT/lib/firmware/isl3877

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/lib/firmware/isl38*

