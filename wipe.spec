Name:           wipe
Version:        2.3.1
Release:        %mkrel 2
Epoch:          0
Summary:        Secure file deletion utility 
License:        GPLv2
Group:          File tools
URL:            http://wipe.sourceforge.net/
Source0:        http://unc.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://unc.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2.sig
Patch0:         %{name}-rootbuildfix.patch
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
Wipe is a tool that effectively degauses the surface of a hard
disk, making it virtually impossible to retrieve the data that was
stored on it. This tool is designed to make sure secure data that is
erased from a hard drive is unrecoverable.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%{makeinstall}
%{__mv} %{buildroot}%{_bindir}/wipe %{buildroot}%{_bindir}/wipe.wipe
%{__mv} %{buildroot}%{_mandir}/man1/wipe.1 %{buildroot}%{_mandir}/man1/wipe.wipe.1

# remove package installed docs
rm -rf %{buildroot}/%{_datadir}/doc/%{name}

%clean
rm -rf %{buildroot}

%post
%{_sbindir}/update-alternatives --install %{_bindir}/wipe wipe %{_bindir}/wipe.wipe 10 --slave %{_mandir}/man1/wipe.1.lzma wipe.1.lzma %{_mandir}/man1/wipe.wipe.1.lzma

%postun
%{_sbindir}/update-alternatives --remove wipe %{_bindir}/wipe.wipe

%files
%defattr(0644,root,root,0755)
%doc LICENSE copyright README CHANGES TODO INSTALL TESTING
%attr(0755,root,root) %{_bindir}/wipe.wipe
%{_mandir}/man1/wipe.wipe.1*


