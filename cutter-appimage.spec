%global debug_package %{nil}
%global __strip /bin/true

Name:           cutter-appimage
Version:        1.12.0
Release:        1%{?dist}
Summary:        GUI for radare2 reverse engineering framework

# # For a breakdown of the licensing, see:
# https://src.fedoraproject.org/rpms/cutter-re/blob/master/f/cutter-re.spec
# https://src.fedoraproject.org/rpms/radare2/blob/master/f/radare2.spec
License:        GPLv3 and CC-BY-SA and CC0 and LGPLv3+ and GPLv2+ and BSD and MIT and ASL 2.0 and MPLv2.0 and zlib

URL:            https://cutter.re
Source0:        https://github.com/radareorg/cutter/releases/download/v%{version}/Cutter-v%{version}-x64.Linux.AppImage
Source1:        https://raw.githubusercontent.com/radareorg/cutter/v%{version}/src/img/cutter.svg
Source2:        https://raw.githubusercontent.com/radareorg/cutter/v%{version}/src/org.radare.Cutter.desktop

ExclusiveArch:  x86_64

%description
Cutter is a Qt and C++ GUI for radare2. Its goal is making an advanced,
customizable and FOSS reverse-engineering platform while keeping the user
experience at mind. Cutter is created by reverse engineers for reverse
engineers.

%prep
%autosetup -cT

install --preserve-timestamps %{SOURCE0} cutter-appimage
install --preserve-timestamps -m 0644 %{SOURCE1} cutter-appimage.svg
install --preserve-timestamps -m 0644 %{SOURCE2} cutter-appimage.desktop

%build
sed -i 's/Name=Cutter/Name=Cutter (AppImage)/' cutter-appimage.desktop
sed -i 's/Exec=Cutter/Exec=cutter-appimage/' cutter-appimage.desktop
sed -i 's/Icon=cutter/Icon=cutter-appimage/' cutter-appimage.desktop

%install
install --preserve-timestamps -D cutter-appimage \
 %{buildroot}%{_bindir}/cutter-appimage
install --mode=644 --preserve-timestamps -D cutter-appimage.svg \
 %{buildroot}%{_datadir}/pixmaps/cutter-appimage.svg
install --mode=644 --preserve-timestamps -D cutter-appimage.desktop \
 %{buildroot}%{_datadir}/applications/cutter-appimage.desktop

%files
%{_bindir}/cutter-appimage
%{_datadir}/pixmaps/cutter-appimage.svg
%{_datadir}/applications/cutter-appimage.desktop

%changelog
* Tue Dec 01 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 1.12.0-1
- Initial package
