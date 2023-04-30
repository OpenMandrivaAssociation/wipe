%undefine _debugsource_packages

Name:           wipe
Version:        2.3.1
Release:        4
Summary:        Secure file deletion utility 
License:        GPLv2
Group:          File tools
URL:            https:://wipe.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2.sig
#Patch0:         %{name}-rootbuildfix.patch
Patch0:		%{name}-honor-cflags.patch
Patch1:		%{name}-fix_install_path.patch
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
Wipe is a tool that effectively degauses the surface of a hard
disk, making it virtually impossible to retrieve the data that was
stored on it. This tool is designed to make sure secure data that is
erased from a hard drive is unrecoverable.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
mv %{buildroot}%{_bindir}/wipe %{buildroot}%{_bindir}/wipe.wipe
mv %{buildroot}%{_mandir}/man1/wipe.1 %{buildroot}%{_mandir}/man1/wipe.wipe.1

# remove package installed docs
rm -rf %{buildroot}/%{_datadir}/doc/%{name}

%post
%{_sbindir}/update-alternatives --install %{_bindir}/wipe wipe %{_bindir}/wipe.wipe 10 --slave %{_mandir}/man1/wipe.1.lzma wipe.1.lzma %{_mandir}/man1/wipe.wipe.1.lzma

%postun
%{_sbindir}/update-alternatives --remove wipe %{_bindir}/wipe.wipe

%files
%doc LICENSE copyright README CHANGES TODO INSTALL TESTING
%{_bindir}/wipe.wipe
%{_mandir}/man1/wipe.wipe.1*

