%define isl3877_version 1.1.0.0
%define isl3886_version 2.7.0.0

Summary:	Firmware for the Linux prism54 driver
Name:		prism54-firmware
Version:	1.0.4.3
Release:	9
Source0:	http://prism54.org/firmware/%{version}.arm
Source1:	http://prism54.org/firmware/%{isl3877_version}.arm
Source2:	http://daemonizer.de/prism54/prism54-fw/fw-softmac/lmac_%{isl3886_version}.arm
License:	Maybe redistributable
Group:		System/Kernel and hardware
Url:		https://wireless.kernel.org/en/users/Drivers/p54#firmware
BuildArch:	noarch


%description
Firmware for the Linux Kernel prism54 driver.

%install
mkdir -p %{buildroot}/lib/firmware
install %{SOURCE0} %{buildroot}/lib/firmware/isl3890
install %{SOURCE1} %{buildroot}/lib/firmware/isl3877
install %{SOURCE1} %{buildroot}/lib/firmware/isl3886

%files
/lib/firmware/isl38*
