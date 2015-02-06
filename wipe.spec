Name:           wipe
Version:        2.3.1
Release:        3
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




%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0:2.3.1-2mdv2011.0
+ Revision: 615437
- the mass rebuild of 2010.1 packages

* Tue Apr 13 2010 Sandro Cazzaniga <kharec@mandriva.org> 0:2.3.1-1mdv2010.1
+ Revision: 534194
- fix license to GPLV2
- remove P1, applied upstream
- new version 2.3.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0:2.2.0-8mdv2010.0
+ Revision: 445816
- rebuild

* Wed Mar 11 2009 Lev Givon <lev@mandriva.org> 0:2.2.0-7mdv2009.1
+ Revision: 353568
- Fix alternatives link to man file.

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0:2.2.0-6mdv2009.0
+ Revision: 261991
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0:2.2.0-5mdv2009.0
+ Revision: 256027
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0:2.2.0-3mdv2008.1
+ Revision: 129367
- kill re-definition of %%buildroot on Pixel's request


* Thu Mar 08 2007 David Walluck <walluck@mandriva.org> 2.2.0-3mdv2007.1
+ Revision: 134929
- spec cleanup
- Import wipe

* Fri Jun 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.2.0-2mdk
- Rebuild

