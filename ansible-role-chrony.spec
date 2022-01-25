%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x01527a34f0d0080f8a5db8d6eb6c5df21b4b6363

%global srcname ansible_role_chrony
%global rolename ansible-role-chrony

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Ansible role to manage chrony

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/ansible-role-chrony
Source0:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires: (python3dist(ansible) or ansible-core >= 2.11)

%description

Ansible role to manage chrony

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{rolename}-%{upstream_version} -S git
#Remove ansible from requirements.txt as dependency on ansible is managed manually
sed -i '/^ansible/d' requirements.txt


%build
%py3_build


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%py3_install


%files
%doc README*
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog
* Tue Jan 25 2022 RDO <dev@lists.rdoproject.org> 1.1.0-1
- Update to 1.1.0

* Thu Oct 21 2021 RDO <dev@lists.rdoproject.org> 1.0.3-1
- Update to 1.0.3


