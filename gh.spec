%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

%global forgeurl https://github.com/cli/cli
Version:         1.11.0

%forgemeta

Name:            gh
Release:         1%{?dist}
Summary:         GitHub's official command line tool
License:         MIT
URL:             %{forgeurl}
Source0:         %{forgesource}

BuildRequires:   golang
BuildRequires:   git

%description
gh is GitHub on the command line. It brings pull requests, issues, and other
GitHub concepts to the terminal next to where you are already working with git
and your code.


%prep
%forgeautosetup


%build
go env -w GOPROXY=https://proxy.golang.org,direct
%make_build bin/gh manpages
mkdir completions
bin/gh completion -s bash > completions/bash
bin/gh completion -s zsh > completions/zsh
bin/gh completion -s fish > completions/fish


%install
%make_install prefix=%{_prefix}
install -m 0755 -vd                   %{buildroot}%{_datadir}/bash-completion/completions
install -m 0644 -vp completions/bash  %{buildroot}%{_datadir}/bash-completion/completions/gh
install -m 0755 -vd                   %{buildroot}%{_datadir}/zsh/site-functions
install -m 0644 -vp completions/zsh   %{buildroot}%{_datadir}/zsh/site-functions/_gh
install -m 0755 -vd                   %{buildroot}%{_datadir}/fish/vendor_completions.d
install -m 0644 -vp completions/fish  %{buildroot}%{_datadir}/fish/vendor_completions.d/gh.fish


%files
%license LICENSE
%doc docs README.md
%{_bindir}/gh
%dir %{_datadir}/bash-completion
%{_datadir}/bash-completion/completions/gh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_gh
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/gh.fish
%{_mandir}/man1/*


%changelog
* Fri May 21 2021 sixg0000d <sixg0000d@gmail.com> - 1.10.2-1
- Update to 1.10.2

* Fri May 21 2021 sixg0000d <sixg0000d@gmail.com> - 1.10.0-1
- Initial package
