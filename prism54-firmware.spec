%define name prism54-firmware
%define version 1.0.4.3
%define isl3877_version 1.1.0.0
%define isl3886_version 2.7.0.0
%define release %mkrel 5

Summary: Firmware for the Linux prism54 driver
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prism54.org/firmware/%{version}.arm
Source1: http://prism54.org/firmware/%{isl3877_version}.arm
Source2: http://daemonizer.de/prism54/prism54-fw/fw-softmac/lmac_%{isl3886_version}.arm
License: Maybe redistributable
Group: System/Kernel and hardware
Url: http://wireless.kernel.org/en/users/Drivers/p54#firmware
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch


%description
Firmware for the Linux Kernel prism54 driver.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/lib/firmware
install %{SOURCE0} %{buildroot}/lib/firmware/isl3890
install %{SOURCE1} %{buildroot}/lib/firmware/isl3877
install %{SOURCE1} %{buildroot}/lib/firmware/isl3886

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/lib/firmware/isl38*

